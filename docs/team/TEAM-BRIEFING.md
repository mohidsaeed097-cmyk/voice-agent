# Team Briefing — Har Department Ne Kya Kiya

> Ye file har member zaroor padhe. Is mein likha hai ke tumhare department ka kaam kya tha, repo mein woh kahan hai, aur **sir poochein to kya bolna hai**.

## Sab se pehle: project ek line mein

Humne ek **voice agent** banaya hai ("Sana"). Tum bolo, wo sune, soche aur awaaz mein jawab de. Wo **live weather** aur **time** bhi batata hai, aur **English aur Urdu** dono samajhta hai.

**Kaise kaam karta hai:**
```
Tum bolte ho → Silero VAD (bolna khatam hua?) → Groq Whisper (awaaz → text)
→ Groq LLM (sochta hai, weather tool chalata hai) → ElevenLabs (text → awaaz) → tum sunte ho
```
**LiveKit** in sab ko real-time mein jodta hai.

---

## Har member ka 15 minute ka kaam (lazmi)

1. Repo apne laptop par clone karo aur agent chalao (README ke steps)
2. Apne department ka section neeche padho
3. Repo mein apne department ki files khol ke dekho
4. "Har member ke 5 sawal" (sab se neeche) yaad karo
5. **QA members:** test cases khud chala ke `docs/qa/test-cases.md` mein Result likhwao

---

## 1. Requirement Gathering (4 members)

**Tumhara kaam kya tha:** ye tay karna ke agent **kya** karega. Sir ki baat (requirement) ko user stories mein badalna, taake Technical ko pata ho kya banana hai aur QA ko pata ho kya test karna hai.

**Repo mein tumhara kaam:**
| File | Kya hai |
| --- | --- |
| `docs/requirements/user-stories.md` | 8 user stories, acceptance criteria aur priority (Must/Should/Could) |
| `docs/requirements/scope.md` | Kya banega, kya nahi banega, aur kyun |
| `docs/requirements/sample-questions.md` | 10 sawal jo agent ko handle karne hain |

**Sir poochein "aapne kya kiya?" to bolo:**
> "Sir, humne requirements gather kin. Aapki baat se 8 user stories banayin, har ek ki acceptance criteria aur priority ke saath. Must stories 4 thin: voice se baat, awaaz mein jawab, live weather, aur har laptop par chalna. Weather wali story US-03 sab se important thi, kyunke us ke liye live data chahiye tha. Humne scope bhi tay kiya: phone calls aur news jaisi cheezein aaj ke sprint se bahar rakhin, taake 1 din mein MVP poora ho. Aur har story ko QA ke test case se link kiya."

**Agar sir poochein:**
- *User story kya hoti hai?* → "As a user, I want..., so that..." format. User ki zaroorat, uske nazariye se.
- *Acceptance criteria kya hai?* → Wo shart jis se pata chale story poori hui ya nahi. Jaise: "galat city par polite error aaye."
- *Must/Should/Could kyun?* → Priority. Pehle Must banaye, waqt bacha to baaqi.

---

## 2. DevOps / Cloud (2 members)

**Tumhara kaam kya tha:** code ka ghar banana (GitHub repo) aur ye pakka karna ke **wahi code har laptop par ek jaisa chale**, aur keys safe rahein.

**Repo mein tumhara kaam:**
| File | Kya hai |
| --- | --- |
| `README.md` | Windows par step-by-step setup |
| `requirements.txt` | Saare packages, ek command se install |
| `.env.example` | Keys ke naam (values nahi) |
| `.gitignore` | `.env` (asli keys) ko GitHub par jaane se rokta hai |
| `docs/devops/common-errors.md` | Har error aur us ka hal |
| `docs/devops/devops-decisions.md` | Humne kya decide kiya aur kyun |
| `.github/ISSUE_TEMPLATE/bug_report.md` | QA ke bug report ka format |

**Sir poochein to bolo:**
> "Sir, maine GitHub repo aur setup banaya. Code ek hai, lekin har laptop apni keys ke saath independently chalta hai. Keys GitHub par na jayein, is liye `.gitignore` lagaya, aur sirf `.env.example` repo mein hai jis mein values nahi. Har laptop par same versions aayein, is liye virtual environment aur `requirements.txt` use kiya. Python 3.12.10 chuna kyunke 3.12 ka wo aakhri version hai jis ka Windows installer hai. Jo bhi setup errors aaye, wo `common-errors.md` mein hal ke saath likhe hain."

**Agar sir poochein:**
- *`.env` kya hai?* → Har laptop ki secret file jis mein API keys hain. GitHub par nahi jati.
- *Virtual environment kyun?* → Project ke packages alag rehte hain, har laptop par same version.
- *Har banda apni key kyun?* → Free limits share na hon, aur key kisi ko bhejni na pade.

---

## 3. Technical (9 members)

**Tumhara kaam kya tha:** asal agent banana: code, tools, personality aur design.

### Core devs (4) → `agent.py`
**Kya kiya:** pipeline banai: `AgentSession` mein VAD + STT + LLM + TTS jode, tools register kiye, greeting lagai.

**Sir ko bolo:**
> "Sir, `agent.py` mein pipeline hai. Silero VAD detect karta hai ke user ne bolna kab band kiya. Groq Whisper awaaz ko text banata hai aur language khud detect karta hai, English ya Urdu. Groq ka LLM `gpt-oss-120b` sochta hai. ElevenLabs Flash v2.5 jawab bolta hai. LiveKit ka `AgentSession` in sab ko real-time mein jodta hai, aur interruption bhi handle karta hai."

### Tool devs (2) → `tools.py`
**Kya kiya:** `get_weather(city)` aur `get_time()` banaye.

**Sir ko bolo:**
> "Sir, LLM ki knowledge ek date tak hai, us ko aaj ka weather nahi pata. Is liye humne **function calling** use ki. `get_weather` ek Python function hai jo Open-Meteo API se pehle city ka latitude/longitude leta hai, phir live weather. LLM khud decide karta hai ke ye function kab chalana hai. Open-Meteo free hai aur key nahi chahiye. Galat city par function saaf message deta hai, taake agent andaza na lagaye."

### Prompt engineer (1) → `prompt.txt`
**Kya kiya:** agent ki personality aur rules likhe.

**Sir ko bolo:**
> "Sir, prompt agent ka behaviour tay karta hai. Naam Sana hai. Jawab 1–3 jumlon mein, kyunke ye bolne wala agent hai. Koi markdown ya emoji nahi, kyunke wo bolne mein ajeeb lagte hain. Sab se important rule: weather aur time ke liye **hamesha tool** use karo, kabhi andaza mat lagao. Aur user jis zabaan mein bole, usi mein jawab do."

### Designers (2) → `docs/design/`
**Kya kiya:** architecture diagram, conversation flow, aur slides.

**Sir ko bolo:**
> "Sir, `architecture.md` mein poori pipeline ka diagram hai, aur ek sequence diagram jo dikhata hai ke weather ka sawal tool tak kaise jata hai. `conversation-flow.md` mein agent ki persona, greeting aur error lines hain. Ye Requirements ki user stories se banaye."

**Technical files:** `agent.py`, `tools.py`, `prompt.txt`, `docs/design/architecture.md`, `docs/design/conversation-flow.md`, `docs/design/how-the-code-works.md`

---

## 4. Quality Assurance (7 members)

**Tumhara kaam kya tha:** sabit karna ke agent wahi karta hai jo stories mein likha hai, **aur har laptop par chalta hai**. QA code nahi likhta. QA test karta hai, bugs pakadta hai, aur har laptop ko Pass/Fail deta hai.

**Repo mein tumhara kaam:**
| File | Kya hai |
| --- | --- |
| `docs/qa/test-cases.md` | 10 test cases, 5 edge cases, 3 security checks, har ek user story se linked |
| `docs/qa/bug-log.md` | 8 asli bugs jo mile, un ki wajah aur fix |
| `docs/qa/laptop-signoff.md` | Har laptop ka Pass/Fail |
| `docs/qa/test-report.md` | Kul nateeja |

**Sir poochein to bolo:**
> "Sir, humne Requirements ki acceptance criteria se 10 test cases banaye, har user story ke liye kam az kam ek. Saath mein edge cases bhi: shor, galat city, internet band, aaj ki news. Testing mein 8 bugs mile. Zyada tar Windows setup ke the: Python PATH, venv active na hona, keys galat copy hona. Ek model ka 404 error tha, wo Technical ne model badal ke fix kiya. Sab bugs `bug-log.md` mein hain. Phir har laptop par 5 demo sawal chala ke sign-off diya, isi liye aap kisi ka bhi laptop utha sakte hain."

**Agar sir poochein:**
- *Test case kya hota hai?* → ID, steps, expected result, aur actual result. Isay chala ke Pass/Fail likhte hain.
- *Sab se bada bug kya tha?* → `404 model_not_found`: Groq account ko wo model nahi mila, default model badal diya.
- *Edge case kya hai?* → Ajeeb ya mushkil haalat jo normal use mein kam aaye, jaise galat city ya shor.

---

## Har member ke 5 sawal (sab ko yaad hone chahiye)

| # | Sawal | Jawab |
| --- | --- | --- |
| 1 | Agent kaise kaam karta hai? | STT (Groq Whisper) awaaz ko text banata hai, LLM (Groq) sochta hai, TTS (ElevenLabs) bolta hai. LiveKit sab jodta hai. |
| 2 | Weather kaise pata chalta hai? | LLM ko khud nahi pata. `get_weather` tool Open-Meteo API se live data lata hai. Isay function calling kehte hain. |
| 3 | Tumhare laptop par kaise chala? | GitHub se clone kiya, apni keys `.env` mein daalin, `pip install -r requirements.txt`, phir `python agent.py console`. |
| 4 | Tumhare department ne kya kiya? | Upar apne department ka jawab. |
| 5 | Scrum kaise follow kiya? | Ek din ka sprint: Sprint Planning, standups, Review aur Retro. Tasks GitHub board par the. Detail: `docs/scrum/sprint-plan.md`. |

**Bonus:**
- *Groq kyun?* → Bohot tez (LPU chip), free tier mein STT aur LLM dono.
- *Har sawal ka jawab deta hai?* → General knowledge haan, weather aur time live. Aaj ki news nahi, us ka tool nahi. Wo agla feature hai.
- *Urdu kaise?* → Whisper language detect karta hai, prompt bolta hai usi zabaan mein jawab do, aur ElevenLabs ka multilingual voice bolta hai.
