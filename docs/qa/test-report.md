# Test Report

**Department:** Quality Assurance
**Version tested:** v1.0

## Summary

| Item | Number |
| --- | --- |
| Functional test cases | 10 (TC-01 to TC-10) |
| Edge cases | 5 (EC-01 to EC-05) |
| Non-functional checks | 3 (NF-01 to NF-03) |
| Automated development checks | 6, all Pass |
| Bugs found | 8 (see [`bug-log.md`](bug-log.md)) |
| Bugs fixed | 8 |
| Open bugs | 0 |
| Laptops signed off | ___ / 23 (see [`laptop-signoff.md`](laptop-signoff.md)) |

Fill the test results in [`test-cases.md`](test-cases.md) and the laptop count above after the final test run.

## What we tested and why

1. **Every user story has at least one test case**, so we can prove the agent does what was asked.
2. **Edge cases** (noise, wrong city, no internet, off-topic) because real users do unexpected things.
3. **Security** — API keys must never reach GitHub.
4. **Every laptop** — sir can pick any laptop, so each one is signed off with the same 5 questions.

## Most important finding

Most bugs (6 of 8) were **setup problems on Windows**, not code problems: Python path, wrong folder, inactive venv, wrongly copied keys. That is why the README and [`../devops/common-errors.md`](../devops/common-errors.md) are detailed, and why every laptop is checked.

## Result

The agent meets all Must stories (US-01 to US-04). Ready for demo once all laptops are signed off.
