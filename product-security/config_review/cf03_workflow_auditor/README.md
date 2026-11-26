# CF-03: CI workflow auditor

**Book chapter:** 7 · **Level:** mid to senior · **Time:** 35 to 40 minutes · **Language:** Python

Implement `audit_workflow(workflow)` in `workflow_auditor.py`. `workflow` is a GitHub Actions workflow as a dict (the YAML key `on` stays `"on"`). Return a sorted list of `(job_name, code)` tuples; use `"workflow"` as the name for workflow-level findings.

| Code | Scope | When |
| --- | --- | --- |
| `UNPINNED_ACTION` | job | a step `uses` a third-party action whose ref is not a 40-character commit SHA. Local actions (`./...`) and `docker://` references are skipped |
| `PWN_REQUEST` | job | the workflow triggers on `pull_request_target` **and** a step checks out code from the pull request (a `with.ref` that mentions `github.event.pull_request.head` or `github.head_ref`) |
| `SCRIPT_INJECTION` | job | a `run` step puts untrusted event text straight into the shell: `${{ github.event.pull_request.title }}`, `.body`, `github.head_ref` or `github.event.issue.title` and similar |
| `BROAD_PERMISSIONS` | workflow | there is no top-level `permissions`, or it is `write-all` |

`on` may be a string, a list or a dict. Never crash on missing keys.

```bash
IMPL=workflow_auditor pytest config_review/cf03_workflow_auditor
```

Talking point: why `pull_request_target` is dangerous (it runs with the base repository's secrets while the checkout is attacker-controlled), and why pinning to a SHA matters (a tag can be moved to different code; a commit SHA cannot).
