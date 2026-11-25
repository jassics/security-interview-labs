# Security Interview Labs

Runnable security interview practice: **spot the vulnerable code** and **coding round problems with solutions**, for product security, application security, cloud and AI security roles.

Every exercise has a vulnerable version, one fix, and a test that proves the exploit works on the vulnerable code and fails on the fixed one. You can run all of it.

> **Warning: this repository contains intentionally vulnerable code.**
> It exists to be read, broken in tests and fixed. Never deploy it, never copy it into a real project, and expect code scanners to flag it. See [SECURITY.md](SECURITY.md).

## What is here

| Folder | Contents | Status |
| --- | --- | --- |
| [`product-security/`](product-security) | Spot-the-vuln in Python, Java and JavaScript; coding round problems, including basic to medium warm-ups in the style of LeetCode and HackerEarth | Pilot: 6 spot-the-vuln and coding exercises, 8 warm-ups |
| [`ai-security/`](ai-security) | Labs for LLM, agent, RAG and model supply chain security | Planned |
| [`market-data/`](market-data) | Dated dataset of public security job postings and pay ranges for 31 target companies, with a refresh method | Snapshot: 25 Nov 2026, 131 postings |

This repository is the full collection. The companion books (Product Security Interview Playbook and AI Security Playbook) use a smaller, curated selection and point here for the rest.

## Run it

Requirements: Python 3.11+, JDK 17+, Node.js 18+.

```bash
cd product-security
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make test
```

Or run `make test` from the repository root.

## Questions from real companies

The goal is to cover the kinds of questions that are publicly discussed for well-known target companies. How that is done, and what is never included, is spelled out in [CONTRIBUTING.md](CONTRIBUTING.md). In short:

- Every exercise is written from scratch. Nothing is copied from an interview, a candidate post or a paid question bank.
- A company tag is added only with a public, linkable source, and it says "reported pattern", not "was asked".
- Nothing covered by an NDA is accepted.

## Related repositories

- [security-study-plan](https://github.com/jassics/security-study-plan): domain-by-domain study checklists
- [security-interview-questions](https://github.com/jassics/security-interview-questions): conceptual and scenario question banks
- [python-for-cybersecurity](https://github.com/jassics/python-for-cybersecurity): Python learning resource for security

## License

[MIT](LICENSE). The exercises are intentionally vulnerable and come with no warranty; see [SECURITY.md](SECURITY.md).
