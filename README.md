# 🎙️ Sana — Voice Agent

**Team Alpha** · Software Project Management · SST · LiveKit + Groq + ElevenLabs

A voice assistant you talk to. Ask anything, the **live weather** of any city, or the **time** — in **English or Urdu** — and it answers out loud.

```
You speak → Silero VAD → Groq Whisper (STT) → Groq LLM ⇄ tools (weather, time) → ElevenLabs (TTS) → you hear
```

> 👥 **Team members: start here → [`docs/team/TEAM-BRIEFING.md`](docs/team/TEAM-BRIEFING.md)**
> It explains what your department did and what to tell sir.

---

## Project documents

| Department | Documents |
| --- | --- |
| Scrum / PM | [Sprint plan](docs/scrum/sprint-plan.md) · [Retrospective](docs/scrum/retrospective.md) |
| Requirement Gathering | [User stories](docs/requirements/user-stories.md) · [Scope](docs/requirements/scope.md) · [Sample questions](docs/requirements/sample-questions.md) |
| Technical | [Architecture](docs/design/architecture.md) · [How the code works](docs/design/how-the-code-works.md) · [Conversation design](docs/design/conversation-flow.md) |
| Quality Assurance | [Test cases](docs/qa/test-cases.md) · [Bug log](docs/qa/bug-log.md) · [Test report](docs/qa/test-report.md) · [Laptop sign-off](docs/qa/laptop-signoff.md) |
| DevOps | [Common errors](docs/devops/common-errors.md) · [DevOps decisions](docs/devops/devops-decisions.md) |

## Code

| File | What it does |
| --- | --- |
| `agent.py` | The agent: connects VAD, STT, LLM and TTS; registers tools; greets the user |
| `tools.py` | `get_weather(city)` (Open-Meteo, live) and `get_time()` |
| `prompt.txt` | Personality and rules (edit to change how it talks) |
| `requirements.txt` | Python packages |
| `.env.example` | Names of the API keys you need (no values) |

---

## Setup on Windows

### 1. Install (one time)

1. **Python 3.12.10** → https://www.python.org/downloads/release/python-31210/ → "Windows installer (64-bit)"
   ⚠️ On the first screen, tick **"Add python.exe to PATH"**. Don't use 3.14.
2. **Git** → https://git-scm.com/download/win
3. Check in a **new** Command Prompt: `python --version` and `git --version`

### 2. Get your own free API keys

| Service | Where | `.env` name |
| --- | --- | --- |
| Groq | https://console.groq.com/keys | `GROQ_API_KEY` |
| ElevenLabs | https://elevenlabs.io → profile → API Keys | `ELEVEN_API_KEY` |
| LiveKit Cloud | https://cloud.livekit.io → project → Settings → API Keys | `LIVEKIT_URL`, `LIVEKIT_API_KEY`, `LIVEKIT_API_SECRET` |

Copy each key with the website's **Copy** button. Never type it by hand, never share it.

### 3. Get the code and install

Open Command Prompt in the folder where you want the project, then:

```
git clone <this-repo-url>
cd voice-agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
notepad .env
```

Paste your keys after the `=` signs (no quotes, no spaces). Save and close.

### 4. Run

```
python agent.py console
```

Speak into your mic. `Ctrl + C` to stop.

**Browser demo:** run `python agent.py dev`, then open your project on https://cloud.livekit.io → **Agents** → **Console** → start a session.

> Opening a new Command Prompt later? Run `venv\Scripts\activate` first (you should see `(venv)`).

### 5. Try it

1. "Hello, who are you?"
2. "What's the weather in Lahore?"
3. "And in London?"
4. "What time is it?"
5. "Lahore ka mausam kaisa hai?"

Problems? → [`docs/devops/common-errors.md`](docs/devops/common-errors.md)

## Get updates

```
git pull
pip install -r requirements.txt
```
