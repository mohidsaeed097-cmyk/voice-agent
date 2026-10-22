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

PROMPT_TEMPLATE = (Path(__file__).parent / "prompt.txt").read_text(encoding="utf-8")

# Voice model. Eleven v3 Conversational is real-time and supports Urdu (and 70+ languages).
# If your ElevenLabs account can't use it, set ELEVEN_MODEL=eleven_flash_v2_5 in .env.
ELEVEN_MODEL = os.getenv("ELEVEN_MODEL", "eleven_v3_conversational")

# Which script the LLM should write Urdu in, so the voice pronounces it naturally:
# - v3 models speak Urdu script directly.
# - Flash v2.5 has no Urdu, but speaks Hindi (Devanagari) script, which sounds like spoken Urdu.
if ELEVEN_MODEL.startswith(("eleven_v3", "eleven_v4")):
    URDU_SCRIPT_RULE = "Write Urdu replies in Urdu script (Nastaliq / Arabic letters), not Roman Urdu and not Devanagari."
else:
    URDU_SCRIPT_RULE = (
        "Write Urdu replies in Devanagari script (the voice engine reads Devanagari naturally and it sounds "
        "like spoken Urdu), but keep the vocabulary Urdu, not Hindi."
    )

PROMPT = PROMPT_TEMPLATE.replace("{URDU_SCRIPT_RULE}", URDU_SCRIPT_RULE)


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=PROMPT,
            tools=[get_weather, get_time],
        )


server = AgentServer()


@server.rtc_session()
async def entrypoint(ctx: agents.JobContext):
    # apply_text_normalization="on": the voice engine spells out any number the LLM still writes as digits.
    tts_options = {"model": ELEVEN_MODEL, "apply_text_normalization": "on"}
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
