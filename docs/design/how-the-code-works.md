# How the Code Works

**Department:** Technical (Core devs, Tool devs, Prompt engineer)

The whole agent is 3 files: `agent.py` (the pipeline), `tools.py` (live data), `prompt.txt` (personality).

## `agent.py` — the pipeline (Core devs)

```python
session = AgentSession(
    vad=silero.VAD.load(),                                        # 1. when did the user stop talking?
    stt=groq.STT(model="whisper-large-v3-turbo", detect_language=True),  # 2. speech -> text (English/Urdu)
    llm=groq.LLM(model="openai/gpt-oss-120b"),                    # 3. think, call tools
    tts=elevenlabs.TTS(model="eleven_flash_v2_5"),                # 4. text -> voice
)
await session.start(room=ctx.room, agent=Assistant())             # start listening
await session.generate_reply(instructions="Greet the user...")    # say hello first
```

Four parts, in order:

1. **Load keys** — `load_dotenv()` reads the member's `.env` file.
2. **`Assistant` class** — gives the agent its instructions (`prompt.txt`) and its tools (`get_weather`, `get_time`).
3. **`AgentSession`** — builds the pipeline: VAD → STT → LLM → TTS.
4. **Greeting** — the agent speaks first.

`agents.cli.run_app(server)` gives us the `console` and `dev` commands.

## `tools.py` — live data (Tool devs)

```python
@function_tool
async def get_weather(city: str) -> str:
    """Get the current live weather for a city."""
```

- `@function_tool` tells LiveKit: "the LLM may call this function".
- The **docstring and the parameter name** are what the LLM reads to decide when to call it — so they are written clearly.
- `get_weather` makes 2 calls to Open-Meteo: city name → latitude/longitude, then latitude/longitude → current weather. It converts the weather code (e.g. `1`) to words ("mainly clear").
- If the city is not found it returns a clear message, so the agent can ask again instead of guessing.
- `get_time` returns the current time in `Asia/Karachi` (Pakistan) by default.

**Function calling, simply:** the LLM doesn't know today's weather. We give it a function. When the user asks about weather, the LLM replies "call `get_weather('Lahore')`", our code runs it, and the LLM turns the result into a sentence.

## `prompt.txt` — personality and rules (Prompt engineer)

- Name **Sana**, friendly, 1–3 sentence answers (it is spoken).
- No markdown, lists or emojis (they sound strange when read aloud).
- **Always call the tool** for weather and time — never guess.
- Reply in the user's language (English or Urdu).
- Be honest when it doesn't know (e.g. today's news).

## Settings without touching code (`.env`)

| Variable | Default | Purpose |
| --- | --- | --- |
| `GROQ_LLM_MODEL` | `openai/gpt-oss-120b` | Change the brain model |
| `ELEVEN_MODEL` | `eleven_flash_v2_5` | Change the voice model |
| `ELEVEN_VOICE_ID` | ElevenLabs default | Choose a different voice |

## How to add a new skill (example: currency rate)

1. Write a new `@function_tool` function in `tools.py`.
2. Add it to `tools=[...]` in `agent.py`.
3. Add one line to `prompt.txt` saying when to use it.

That is the same pattern we used for weather — this is how the agent can grow.
