# Security policy

## This repository is vulnerable on purpose

Files named `*_vulnerable.*`, `Vulnerable*.java` and similar contain deliberate security flaws for teaching. Their tests demonstrate each flaw using harmless stand-ins (marker functions, temporary files, `echo`).

Please do not report these as vulnerabilities. Automated scanners (Dependabot, CodeQL, secret scanning) may flag them; that is expected.

## What is a real issue

Please report privately through GitHub's "Report a vulnerability" feature if you find:

- a *fixed* version that is still exploitable, or a fix that teaches a bad pattern
- a test that does something outside its own temporary files or marker functions
- a real secret, credential or personal data committed by mistake
- a dependency issue in the tooling around the exercises (Makefile, test setup)

Fixes to teaching content (a clearer hint, a better fix) are welcome as normal pull requests.
