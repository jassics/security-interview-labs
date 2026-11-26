def _pod_spec(manifest):
    if not isinstance(manifest, dict):
        return {}
    if manifest.get("kind") == "Deployment":
        return (((manifest.get("spec") or {}).get("template") or {}).get("spec")) or {}
    return manifest.get("spec") or {}


def _has_digest(image):
    return "@sha256:" in image


def _mutable(image):
    if _has_digest(image):
        return False
    last = image.rsplit("/", 1)[-1]
    if ":" not in last:
        return True
    return last.rsplit(":", 1)[1] == "latest"


def lint_manifest(manifest):
    spec = _pod_spec(manifest)
    findings = set()
    pod_ctx = spec.get("securityContext") or {}

    for flag in ("hostNetwork", "hostPID", "hostIPC"):
        if spec.get(flag) is True:
            findings.add(("pod", "HOST_ACCESS"))
    for vol in spec.get("volumes") or []:
        if isinstance(vol, dict) and "hostPath" in vol:
            findings.add(("pod", "HOST_PATH"))

    containers = (spec.get("containers") or []) + (spec.get("initContainers") or [])
    for c in containers:
        if not isinstance(c, dict):
            continue
        name = c.get("name", "?")
        ctx = c.get("securityContext") or {}
        if ctx.get("privileged") is True:
            findings.add((name, "PRIVILEGED"))
        run_as_user = ctx.get("runAsUser", pod_ctx.get("runAsUser"))
        non_root = ctx.get("runAsNonRoot", pod_ctx.get("runAsNonRoot"))
        if run_as_user == 0 or non_root is not True:
            findings.add((name, "RUNS_AS_ROOT"))
        if ctx.get("allowPrivilegeEscalation") is not False:
            findings.add((name, "PRIV_ESCALATION"))
        dropped = [str(x).upper() for x in (ctx.get("capabilities") or {}).get("drop") or []]
        if "ALL" not in dropped:
            findings.add((name, "CAPS_NOT_DROPPED"))
        if _mutable(str(c.get("image", ""))):
            findings.add((name, "MUTABLE_IMAGE"))
        if not (c.get("resources") or {}).get("limits"):
            findings.add((name, "NO_LIMITS"))
    return sorted(findings)
