# CF-02: Pod spec linter

**Book chapter:** 6 · **Level:** mid · **Time:** 30 to 35 minutes · **Language:** Python

Implement `lint_manifest(manifest)` in `pod_spec_linter.py`. `manifest` is a Kubernetes `Pod` or `Deployment` as a dict (JSON form; the YAML you know maps one to one). Return a sorted list of `(scope, code)` tuples, where `scope` is a container name, or `"pod"` for pod-level findings.

| Code | Scope | When |
| --- | --- | --- |
| `PRIVILEGED` | container | `securityContext.privileged` is true |
| `RUNS_AS_ROOT` | container | `runAsUser` is 0, or neither the container nor the pod sets `runAsNonRoot: true` |
| `PRIV_ESCALATION` | container | `allowPrivilegeEscalation` is not explicitly `false` |
| `CAPS_NOT_DROPPED` | container | `capabilities.drop` does not include `ALL` |
| `MUTABLE_IMAGE` | container | image has no tag, or the tag is `latest`, and no `@sha256:` digest |
| `NO_LIMITS` | container | `resources.limits` is missing |
| `HOST_ACCESS` | pod | `hostNetwork`, `hostPID` or `hostIPC` is true |
| `HOST_PATH` | pod | any volume uses `hostPath` |

A `Deployment` keeps its pod spec at `spec.template.spec`; a `Pod` at `spec`. Check `containers` and `initContainers`. Never crash on missing keys.

```bash
IMPL=pod_spec_linter pytest config_review/cf02_pod_spec_linter
```

Talking point: these are the checks behind the Pod Security Standards ideas in Chapter 6. Know that policy engines (admission control) enforce them at deploy time, and a linter in CI only advises.
