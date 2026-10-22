# Sprint Plan

**Scrum Master / Project Manager:** Mohid

## Sprint goal

> By the end of the day, every team member's laptop runs a voice agent that answers spoken questions — including the live weather.

## Team

| Department | Members | Responsible for |
| --- | --- | --- |
| DevOps / Cloud | 2 | Repo, setup, README, keys safety, release |
| Requirement Gathering | 4 | User stories, scope, sample questions |
| Technical | 9 (4 core devs, 2 tool devs, 1 prompt engineer, 2 designers) | Code, tools, prompt, architecture, slides |
| Quality Assurance | 7 (1 lead, 6 testers) | Test cases, bug reports, laptop sign-off |

## Sprint timeline

| Phase | Time | What happens | Output |
| --- | --- | --- | --- |
| 0. Prep | Day before | Install Python, Git; create accounts and keys; repo created | Repo + setup ready |
| 1. Sprint Planning | T+0:00–0:30 | Goal, backlog, tasks assigned | Board with owners |
| 2. Build | T+0:30–3:00 | Stories written; agent, tools and prompt built | Agent talks on one laptop |
| Standup 1 | T+3:00 | Leads: done / next / blocked | Blockers list |
| 3. Integrate & Test | T+3:00–5:00 | Merge to `main`, QA testing, bugs fixed | v1.0 candidate |
| Standup 2 | T+5:00 | Leads: done / next / blocked | Go for rollout |
| 4. Rollout | T+5:00–7:30 | Every member clones and runs; QA signs off each laptop | All laptops Pass |
| 5. Review + Retro | T+7:30–8:00 | Demo to sir; retrospective | Retro notes |

## Product backlog

See [`../requirements/user-stories.md`](../requirements/user-stories.md). Must: US-01–US-04. Should: US-05. Could: US-06–US-08.

## Definition of Done

A story is Done when:
- [x] Code is in `main` on GitHub
- [x] No API key is in the repo
- [x] QA test case for it passes
- [x] It runs on a laptop other than the developer's
- [x] README updated if setup changed

## Scrum artifacts in this repo

| Artifact | Where |
| --- | --- |
| Product backlog | `docs/requirements/user-stories.md` + GitHub Projects board |
| Sprint backlog | GitHub Projects board |
| Increment | `main` branch, release `v1.0` |
| Bugs | GitHub Issues + `docs/qa/bug-log.md` |
| Retrospective | `docs/scrum/retrospective.md` |
