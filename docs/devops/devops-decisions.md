# DevOps Decisions

**Department:** DevOps / Cloud

## What DevOps set up

| Item | What it does | File |
| --- | --- | --- |
| GitHub repository | One place for all code and documents; every member clones it | the repo |
| Dependencies list | One command installs everything: `pip install -r requirements.txt` | `requirements.txt` |
| Key template | Lists key names (no values); each member copies it to `.env` | `.env.example` |
| Secret protection | Stops `.env` (real keys) and `venv` from being uploaded | `.gitignore` |
| Setup guide | Step-by-step Windows setup | `README.md` |
| Error guide | Every error we hit and its fix | `docs/devops/common-errors.md` |
| Bug template | Standard format for QA bug reports | `.github/ISSUE_TEMPLATE/bug_report.md` |
| Release | Final version tagged `v1.0` | GitHub → Releases |

## Key decisions and why

| Decision | Why |
| --- | --- |
| **Each member uses their own API keys** | Free tiers have limits; sharing one key would run out. Also safer — no key is passed around |
| **Keys never go to GitHub** (`.gitignore`) | A leaked key can be abused and the account blocked |
| **Python 3.12.10** | Last 3.12 release with a Windows installer; 3.14 is too new for some libraries |
| **Virtual environment (`venv`)** | Keeps project packages separate, so every laptop has the same versions |
| **Pinned framework version** (`livekit-agents~=1.8`) | Every laptop installs a compatible version |
| **Model names configurable in `.env`** | If a model is unavailable for an account, change one line — no code change |
| **Open-Meteo for weather** | Free, no API key, so 19 people don't need another account |
| **Two run modes** (console / dev) | Console needs nothing but the laptop; dev mode gives a browser demo through LiveKit Cloud |

## Deployment model

Code is the same everywhere; each laptop is an independent deployment using its owner's keys:

```
GitHub repo (one code base)
   ├── git clone → Laptop 1 (+ member 1's keys) → agent runs
   ├── git clone → Laptop 2 (+ member 2's keys) → agent runs
   └── ... 19 laptops
```
