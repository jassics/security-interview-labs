import re

SHA = re.compile(r"^[0-9a-f]{40}$")
UNTRUSTED = re.compile(
    r"\$\{\{\s*github\.(event\.(pull_request|issue|comment)\.(title|body)|head_ref|event\.head_commit\.message)"
)


def _triggers(workflow):
    on = workflow.get("on")
    if isinstance(on, str):
        return {on}
    if isinstance(on, list):
        return set(map(str, on))
    if isinstance(on, dict):
        return set(on)
    return set()


def audit_workflow(workflow):
    if not isinstance(workflow, dict):
        return []
    findings = set()
    perms = workflow.get("permissions")
    if perms is None or perms == "write-all":
        findings.add(("workflow", "BROAD_PERMISSIONS"))
    prt = "pull_request_target" in _triggers(workflow)

    for job_name, job in (workflow.get("jobs") or {}).items():
        if not isinstance(job, dict):
            continue
        for step in job.get("steps") or []:
            if not isinstance(step, dict):
                continue
            uses = step.get("uses")
            if isinstance(uses, str) and not uses.startswith(("./", "docker://")):
                ref = uses.split("@", 1)[1] if "@" in uses else ""
                if not SHA.match(ref):
                    findings.add((job_name, "UNPINNED_ACTION"))
            ref_in = str((step.get("with") or {}).get("ref", ""))
            if prt and isinstance(uses, str) and uses.startswith("actions/checkout") and (
                "github.event.pull_request.head" in ref_in or "github.head_ref" in ref_in
            ):
                findings.add((job_name, "PWN_REQUEST"))
            run = step.get("run")
            if isinstance(run, str) and UNTRUSTED.search(run):
                findings.add((job_name, "SCRIPT_INJECTION"))
    return sorted(findings)
