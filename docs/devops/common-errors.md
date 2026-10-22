# Common Errors and Fixes (Windows)

**Department:** DevOps

| Error message | What it means | Fix |
| --- | --- | --- |
| `Python was not found; run without arguments to install from the Microsoft Store` | Python is not installed, or not on PATH | Install Python 3.12.10 (link in README), tick **"Add python.exe to PATH"**. If it still fails: Settings → Apps → Advanced app settings → App execution aliases → turn **off** python.exe and python3.exe |
| `The system cannot find the path specified` | You are in the wrong folder | Open the project folder in File Explorer, type `cmd` in the address bar, press Enter. Run `dir` — you should see `agent.py` |
| `'pip' is not recognized` | Virtual environment not active | `venv\Scripts\activate` (you should see `(venv)` at the start of the line) |
| `ModuleNotFoundError: No module named 'dotenv'` (or any module) | New window, venv not active | `venv\Scripts\activate`, then run again. No need to reinstall |
| `running scripts is disabled on this system` | PowerShell security policy | Use Command Prompt (cmd) instead, or run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once |
| `401 ... Invalid API Key` | A key in `.env` is wrong | Make a new key on the website, copy with the **Copy** button, paste into `.env`. Never type keys by hand |
| `404 ... model ... does not exist or you do not have access` | Your Groq account can't use that model | In `.env`: `GROQ_LLM_MODEL=openai/gpt-oss-120b` (or `llama-3.1-8b-instant`) |
| Changed `.env` but nothing changed | The line starts with `#` (a comment) | Remove the `#` so the line starts with the variable name |
| Agent can't hear you | Microphone permission | Settings → Privacy & security → Microphone → allow desktop apps; check the correct mic is selected |
| Agent doesn't speak | Volume, or ElevenLabs key/credits | Check volume; make a new ElevenLabs key; keep tests short to save credits |
| "The weather service is not reachable" | No internet | Check Wi-Fi or use a mobile hotspot |
| Long wait on first start | Models are loading | Wait 20–60 seconds the first time |
