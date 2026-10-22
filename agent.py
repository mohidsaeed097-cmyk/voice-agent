"""
Voice Agent — LiveKit + Groq + ElevenLabs

Pipeline:
    mic -> Silero VAD (detects when you stop talking)
        -> Groq Whisper (speech-to-text)
        -> Groq Llama (thinks, calls tools)
        -> ElevenLabs (text-to-speech)
        -> speaker

Run:
    python agent.py console   # talk to it in your terminal (mic + speakers)
    python agent.py dev       # connect to LiveKit Cloud, talk via the browser
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentServer, AgentSession
from livekit.plugins import elevenlabs, groq, silero

from tools import get_time, get_weather

load_dotenv(Path(__file__).parent / ".env")

PROMPT = (Path(__file__).parent / "prompt.txt").read_text(encoding="utf-8")


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=PROMPT,
            tools=[get_weather, get_time],
        )


server = AgentServer()


@server.rtc_session()
async def entrypoint(ctx: agents.JobContext):
    # Flash v2.5 is multilingual: it reads the reply text and speaks
    # English or Hindi/Urdu automatically, and it is ElevenLabs' fastest model.
    tts_options = {"model": os.getenv("ELEVEN_MODEL", "eleven_flash_v2_5")}
    if os.getenv("ELEVEN_VOICE_ID"):
        tts_options["voice_id"] = os.getenv("ELEVEN_VOICE_ID")

    session = AgentSession(
        vad=silero.VAD.load(),
        # detect_language=True: Whisper works out whether the user spoke English or Urdu
        stt=groq.STT(model="whisper-large-v3-turbo", detect_language=True),
        llm=groq.LLM(model=os.getenv("GROQ_LLM_MODEL", "openai/gpt-oss-120b"), temperature=0.6),
        tts=elevenlabs.TTS(**tts_options),
    )

    await session.start(room=ctx.room, agent=Assistant())

    await session.generate_reply(
        instructions="Greet the user in one short sentence, say your name, and mention you can tell the weather and the time."
    )


if __name__ == "__main__":
    agents.cli.run_app(server)
