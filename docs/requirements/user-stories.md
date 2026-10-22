# User Stories — Voice Agent

**Department:** Requirement Gathering
**Priority scale:** Must (MVP, ship today) · Should (important) · Could (if time allows)

The client brief (from sir): *"Build a voice agent. We ask it anything — for example, how the weather is — and it answers by voice. Use LiveKit, Groq and ElevenLabs. It must run on every team member's laptop."*

From that brief we wrote 8 user stories.

| ID | User story | Acceptance criteria | Priority | Status |
| --- | --- | --- | --- | --- |
| US-01 | As a user, I want to talk to the agent with my voice, so that I don't have to type. | The agent hears speech from the laptop mic (terminal) or browser, and turns it into correct text. | Must | Done |
| US-02 | As a user, I want the agent to answer out loud, so that it feels like a real conversation. | The reply is spoken in a natural voice, starts within about 3 seconds, and is 1–3 sentences long. | Must | Done |
| US-03 | As a user, I want to ask the live weather of any city, so that I get real, current information. | "What's the weather in Lahore?" returns current temperature and condition from a live source. An unknown city gets a polite error, not a made-up answer. | Must | Done |
| US-04 | As a team member, I want to run the agent on my own laptop, so that I can demo it to sir. | A fresh Windows laptop goes from `git clone` to a talking agent by following the README only, in about 15 minutes. | Must | Done |
| US-05 | As a user, I want the agent to greet me and tell me what it can do, so that I know how to use it. | First line says the agent's name and mentions weather and time. | Should | Done |
| US-06 | As a user, I want to ask the current time and date, so that I get a correct answer. | Returns the correct current Pakistan time. | Could | Done |
| US-07 | As a user, I want to speak in Urdu, so that I can use my own language. | An Urdu question gets a sensible spoken answer in Urdu; an English question still gets English. | Could | Done |
| US-08 | As a user, I want to stop the agent mid-sentence by speaking, so that I don't have to wait. | When I talk while it speaks, it stops and listens to the new question. | Could | Done (built into LiveKit) |

## Why these priorities

- **US-01 to US-04 are Must** because without them there is no working demo: sir asked for a voice agent, live answers (weather), and it running on every laptop.
- **US-03 is the key story.** It is what makes this an *agent* and not just a chatbot — it needs live data the AI model does not have (see the Technical docs: function calling).
- **US-06 to US-08 are Could** — added only after the Must stories worked.

## Traceability

Every story maps to QA test cases in [`../qa/test-cases.md`](../qa/test-cases.md):

| Story | Test cases |
| --- | --- |
| US-01 | TC-01 |
| US-02 | TC-02 |
| US-03 | TC-03, TC-04, TC-05 |
| US-04 | TC-10 |
| US-05 | TC-06 |
| US-06 | TC-07 |
| US-07 | TC-08 |
| US-08 | TC-09 |
