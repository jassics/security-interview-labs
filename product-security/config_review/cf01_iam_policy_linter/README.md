# CF-01: IAM policy linter

**Book chapter:** 5 · **Level:** mid · **Time:** 30 minutes · **Language:** Python

Implement `lint_policy(policy)` in `iam_policy_linter.py`. `policy` is an AWS-style policy document as a dict. Return a sorted list of `(statement_index, code)` tuples.

| Code | When |
| --- | --- |
| `ADMIN_ALL` | `Allow` with `Action` `*` and `Resource` `*` |
| `WILDCARD_ACTION` | `Allow` with `*` or `service:*` in `Action` (not already `ADMIN_ALL`) |
| `WILDCARD_RESOURCE` | `Allow` with `Resource` `*` and at least one action other than `sts:GetCallerIdentity` (not already `ADMIN_ALL`) |
| `PUBLIC_PRINCIPAL` | `Allow` with `Principal` `*` (or `{"AWS": "*"}`) and no `Condition` |
| `PASSROLE_WILDCARD` | `Allow` including `iam:PassRole` with `Resource` `*` |
| `NOT_ACTION_ALLOW` | `Allow` that uses `NotAction` |

Rules: `Statement` may be one dict or a list; `Action`, `Resource` may be a string or a list; action names are case-insensitive; `Deny` statements are ignored; never crash on missing keys.

```bash
IMPL=iam_policy_linter pytest config_review/cf01_iam_policy_linter
```

Open `iam_policy_linter_solution.py` only after you have tried. Talking point: a linter finds patterns; it cannot tell you whether `s3:*` on one bucket is intended. Ask what the policy is *for*.
