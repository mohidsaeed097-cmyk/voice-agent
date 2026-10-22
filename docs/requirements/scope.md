# Scope — Voice Agent (1-day sprint)

**Department:** Requirement Gathering

## Goal

By the end of the sprint, every team member's laptop runs a voice agent that answers spoken questions — including the live weather — out loud.

## In scope (built today)

- Talk to the agent by voice (terminal or browser)
- Spoken answers in a natural voice
- Live weather for any city (Open-Meteo, free, no key)
- Current time and date (Pakistan time by default)
- General knowledge questions
- English and Urdu (bilingual: replies in the language you speak)
- Runs on Windows laptops, each with the member's own API keys

## Out of scope (not today — moved to the backlog)

| Idea | Why not today |
| --- | --- |
| Phone calls to a real number | Needs a paid phone number |
| Memory between sessions | Extra storage design; not in the brief |
| Today's news / web search | Needs another tool; next sprint |
| Mobile app or custom website | Frontend work; next sprint |
| Cloning someone's own voice | Paid ElevenLabs plan |

## Constraints

| Constraint | Effect on design |
| --- | --- |
| 1-day deadline | Small MVP, 3 core features |
| Free tools only | Groq free tier, ElevenLabs free tier, LiveKit Cloud free, Open-Meteo |
| Mostly Windows laptops | Windows-first README and error guide |
| 19 laptops | Every member uses their own keys so free limits are not shared |

## Tools required by the client (sir)

| Tool | Used for |
| --- | --- |
| LiveKit | Real-time audio + agent framework (connects everything) |
| Groq | Speech-to-text (Whisper) and the LLM brain |
| ElevenLabs | Text-to-speech (the voice) |

Note: sir said "Grok". We used **Groq** (groq.com), the fast AI inference platform commonly used for voice agents. Grok is a different product (xAI chatbot).
