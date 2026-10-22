# Bug Log

**Department:** Quality Assurance (with DevOps and Technical for fixes)

These are the real problems found while building and running the agent on Windows, and how each was fixed.

| ID | Bug / problem | Where it showed | Root cause | Fix | Fixed by | Status |
| --- | --- | --- | --- | --- | --- | --- |
| BUG-01 | `Python was not found` | Fresh Windows laptop | Python not installed; Windows opened the Microsoft Store shortcut instead | Install Python 3.12.10 with "Add python.exe to PATH" ticked; README updated | DevOps | Closed |
| BUG-02 | No Windows installer for latest Python 3.12 | python.org | 3.12 is in security-only mode; 3.12.10 is the last version with an installer | README now links the exact 3.12.10 installer | DevOps | Closed |
| BUG-03 | `The system cannot find the path specified` / `'pip' is not recognized` | Command Prompt | Commands were run in `C:\Users\<name>`, not in the project folder | README: open the project folder, type `cmd` in the address bar | DevOps | Closed |
| BUG-04 | `ModuleNotFoundError: No module named 'dotenv'` | New terminal window | The virtual environment was not active in the new window | Always run `venv\Scripts\activate` first; added to README | DevOps | Closed |
| BUG-05 | `401 Invalid API Key` (Groq) | Running the agent | Key was typed from a screenshot; `I` and `l` look the same | Always use the website's Copy button; never retype keys | QA | Closed |
| BUG-06 | `404 model_not_found` for `llama-3.3-70b-versatile` | First spoken question | That model was not available to the new Groq account | Default model changed to `openai/gpt-oss-120b`; can be changed in `.env` | Technical | Closed |
| BUG-07 | Model change in `.env` had no effect | `.env` file | The line started with `#`, so it was treated as a comment | Remove `#` from the line; documented in common errors | QA | Closed |
| BUG-08 | Agent only understood English | Urdu question | STT language was fixed to `en`; voice model did not support Urdu | Language auto-detect in STT, bilingual prompt, multilingual voice model | Technical | Closed |
| BUG-09 | Urdu replies sounded like Hindi, and the voice stumbled on numbers ("27 °C") | TC-08, Urdu weather question | Replies were written in Devanagari script, which pulled the model toward Hindi words; digits and symbols like ° were read awkwardly | Voice model changed to Eleven v3 Conversational (supports Urdu); LLM now writes Urdu in Urdu script with Urdu vocabulary; all numbers written as words; voice text normalization turned on | Technical | Closed (retest Pass) |

## How to report a new bug

Open a GitHub Issue → **Bug report** template → fill: steps, expected, actual, screenshot. Label: `bug`.
