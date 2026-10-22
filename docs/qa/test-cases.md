# Test Cases

**Department:** Quality Assurance
**Based on:** acceptance criteria in [`../requirements/user-stories.md`](../requirements/user-stories.md)

**How to run:** activate the venv, run `python agent.py console`, say each line, and fill the **Result** column with Pass or Fail (+ a note if Fail). If something fails, open a GitHub Issue using the Bug report template.

## Functional tests

| ID | Story | Steps | Expected result | Result | Tested by |
| --- | --- | --- | --- | --- | --- |
| TC-01 | US-01 | Say "Hello, who are you?" | The transcript shows the question correctly | | |
| TC-02 | US-02 | Ask "What is Python?" | Spoken answer, starts within ~3 seconds, 1–3 sentences | | |
| TC-03 | US-03 | Say "What's the weather in Lahore?" | Live temperature and condition for Lahore | | |
| TC-04 | US-03 | Then say "And in London?" | Understands follow-up, gives London weather | | |
| TC-05 | US-03 | Say "What's the weather in Xyzabc?" | Polite "couldn't find that city"; no invented weather | | |
| TC-06 | US-05 | Start the agent | Greets with its name and mentions weather and time | | |
| TC-07 | US-06 | Say "What time is it?" | Correct current Pakistan time | | |
| TC-08 | US-07 | Say "Lahore ka mausam kaisa hai?" | Answers in Urdu with live weather | | |
| TC-09 | US-08 | Start a long question, then interrupt while it speaks | Agent stops and listens to the new question | | |
| TC-10 | US-04 | On a fresh laptop, follow the README only | Agent runs in about 15 minutes | | |

## Edge cases

| ID | Steps | Expected result | Result | Tested by |
| --- | --- | --- | --- | --- |
| EC-01 | Ask with background noise (fan, talking) | Still understands, or asks to repeat | | |
| EC-02 | Ask a very long question | Still answers briefly | | |
| EC-03 | Ask "Who won today's cricket match?" | Says honestly it doesn't have today's news | | |
| EC-04 | Turn Wi-Fi off, ask weather | Says weather service is not reachable (no crash) | | |
| EC-05 | Say nothing for 30 seconds | Agent waits quietly, does not talk on its own | | |

## Non-functional checks

| ID | Check | Expected | Result |
| --- | --- | --- | --- |
| NF-01 | API keys are not in the GitHub repo | Only `.env.example` (no values) is in the repo | |
| NF-02 | `.env` is ignored by Git | `.gitignore` contains `.env` | |
| NF-03 | Response time | Typical reply starts within ~3 seconds | |

## Automated checks done during development

These were run on the code before release:

| Check | Result |
| --- | --- |
| `agent.py` imports and loads all plugins (LiveKit, Groq, ElevenLabs, Silero) | Pass |
| Both tools (`get_weather`, `get_time`) register with the agent | Pass |
| `get_time()` returns the Pakistan time string | Pass |
| `get_weather("Lahore")` builds a correct sentence from a sample API response | Pass |
| `get_weather("Xyz")` returns "I could not find a city called Xyz." for an unknown city | Pass |
| `python agent.py --help` shows `console` and `dev` commands | Pass |
