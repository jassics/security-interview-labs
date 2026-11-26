# SV-06: Broken object-level authorization and mass assignment

**Book chapter:** 3 (API security), also 2 · **Level:** fresher to mid · **Language:** Python · **CWE:** CWE-639, CWE-915

## Scenario

A small orders API has two handlers: `get_order` (`GET /orders/{id}`) and `update_profile` (`PATCH /me`). The caller is already authenticated. Read `bola_vulnerable.py` and list every problem before you open anything else.

## Hints

1. The caller is logged in. Is the *object* theirs?
2. What does `update_profile` do with whatever JSON arrives?

## What an interviewer listens for

- Names the first bug as BOLA (OWASP API1): authentication is not authorization; check ownership on every object access, on the server.
- Names the second as mass assignment: bind only an allowlist of fields; never let a client set `role` or `owner_id`.
- Mentions returning the same error for "missing" and "not yours", and that random IDs help but are not the control.

## The fix

See `bola_fixed.py`: an ownership check that returns the same answer for missing and not-yours, and a field allowlist that rejects anything else.

## Run

```bash
pytest spot_the_vuln/python/06_bola_mass_assignment
```
