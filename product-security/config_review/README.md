# Configuration review exercises (CF-01 to CF-03)

Small, dependency-free exercises for the cloud, Kubernetes and pipeline chapters of the playbook. Each exercise gives you a stub to implement, tests, and a reference solution.

| ID | What you build | Book chapter |
| --- | --- | --- |
| CF-01 | IAM policy linter (wildcards, public principals, `iam:PassRole`) | 5 |
| CF-02 | Pod spec linter (privileged, root, host access, mutable tags, limits) | 6 |
| CF-03 | CI workflow auditor (unpinned actions, risky triggers, script injection, broad permissions) | 7 |

Inputs are plain JSON-style dictionaries so the exercises need no extra packages. In real work you would parse YAML or JSON from the repository first.

```bash
IMPL=iam_policy_linter pytest config_review/cf01_iam_policy_linter    # your version
pytest config_review                                                  # reference solutions
```

These are teaching linters, not products. Use a real tool in practice (for example Checkov, kube-linter or zizmor) and know what yours would miss.
