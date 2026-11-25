# Contributing

Thanks for helping. This page covers two things: how exercises are structured, and the rules for anything tied to a specific company.

## Exercise structure

Each exercise is a folder with the same shape:

| File | Purpose |
| --- | --- |
| `README.md` | Scenario, hints, what an interviewer listens for, the fix explained, the same bug in other languages |
| `*_vulnerable.*` | The code to review |
| `*_fixed.*` | One reasonable fix |
| test or check file | Proves the exploit works on the vulnerable version and fails on the fixed one |

Rules for the code:

- Exploits must be harmless: marker functions, temporary files, `echo`. Never touch the network, the user's files or real services.
- No pinned vulnerable library versions. Use small self-contained simulations instead.
- Tests must pass with `make test` and must fail if the fix is broken.
- Use unique module names per exercise (for example `pickle_session_fixed.py`), so test runs do not collide.

## Company-tagged questions

Candidates want to know what companies ask. This repository covers that, carefully.

**What a company tag means.** A tag says "this pattern is reported in public sources for this company". It never says "this exact question was asked". Interview content changes, and candidate reports are often wrong.

**What is required to add a tag.**

1. A public, linkable source: the company's own engineering or security blog, a published candidate guide, a conference talk, or a candidate write-up posted publicly.
2. The source URL and the date you accessed it, recorded in the exercise's README under "Public sources".
3. An exercise you wrote yourself, covering the *pattern* (the bug class, the problem type, the system design theme), not the wording.

**What is never accepted.**

- Questions copied or closely paraphrased from interviews, Glassdoor-style posts, paid question banks, or leaked material.
- Anything you saw under an NDA, including your own interviews or your employer's interviews.
- Claims of "asked at Company X" without a public source.
- Non-public information about any company's hiring process.

**Removal.** If a company or rights holder asks for something to be removed, open an issue or contact the maintainer, and it will be removed.

Company names appear only to describe patterns in public material. They imply no affiliation with or endorsement by those companies.

## Pull request checklist

- [ ] Exercise folder has all four files
- [ ] `make test` passes
- [ ] The test fails when the fix is deliberately broken
- [ ] Exploits are harmless and local
- [ ] Any company tag has a public source and access date
- [ ] You wrote it yourself
