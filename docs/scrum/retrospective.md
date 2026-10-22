# Sprint Retrospective

**Scrum Master:** Mohid

## What went well

- The full pipeline (LiveKit + Groq + ElevenLabs) worked end to end in one day.
- Function calling solved the "LLM doesn't know today's weather" problem cleanly.
- Every problem we hit was written down (`docs/qa/bug-log.md`), so later laptops were faster to set up.
- Keys stayed off GitHub; every member used their own.

## What could be better

- Most time went to Windows setup (Python, PATH, venv), not to code.
- Keys copied from screenshots caused `401` errors.
- A model unavailable on a new Groq account caused a `404`; we should check model access first.

## Actions for the next sprint

| Action | Owner |
| --- | --- |
| Do setup (Python, Git, accounts) the day before | DevOps |
| Always copy keys with the Copy button | All |
| Add a web search / news tool | Technical |
| Add memory between sessions | Technical |
| Build a custom web page for the agent | Technical — Design |

_Add the team's own points here after the review._
