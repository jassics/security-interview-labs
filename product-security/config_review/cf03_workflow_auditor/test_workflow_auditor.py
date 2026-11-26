import importlib
import os

impl = importlib.import_module(os.environ.get("IMPL", "workflow_auditor_solution"))
audit = impl.audit_workflow

SHA = "a" * 40


def wf(steps, on="push", permissions=None, job="build"):
    out = {"on": on, "jobs": {job: {"steps": steps}}}
    if permissions is not None:
        out["permissions"] = permissions
    return out


def test_clean_workflow():
    w = wf([{"uses": f"actions/checkout@{SHA}"}, {"run": "make test"}], permissions={"contents": "read"})
    assert audit(w) == []


def test_unpinned_action_tag_and_branch():
    w = wf([{"uses": "actions/checkout@v4"}, {"uses": "some/action@main"}], permissions={"contents": "read"})
    assert audit(w) == [("build", "UNPINNED_ACTION")]


def test_local_and_docker_actions_are_skipped():
    w = wf([{"uses": "./.github/actions/setup"}, {"uses": "docker://alpine:3.20"}],
           permissions={"contents": "read"})
    assert audit(w) == []


def test_missing_or_write_all_permissions():
    assert audit(wf([{"run": "true"}])) == [("workflow", "BROAD_PERMISSIONS")]
    assert audit(wf([{"run": "true"}], permissions="write-all")) == [("workflow", "BROAD_PERMISSIONS")]


def test_pwn_request():
    steps = [{"uses": f"actions/checkout@{SHA}",
              "with": {"ref": "${{ github.event.pull_request.head.sha }}"}}]
    w = wf(steps, on={"pull_request_target": {}}, permissions={"contents": "read"})
    assert audit(w) == [("build", "PWN_REQUEST")]
    safe = wf(steps, on="pull_request", permissions={"contents": "read"})
    assert audit(safe) == []


def test_script_injection():
    steps = [{"run": 'echo "${{ github.event.pull_request.title }}"'}]
    assert audit(wf(steps, permissions={"contents": "read"})) == [("build", "SCRIPT_INJECTION")]
    ok = [{"run": 'echo "$TITLE"', "env": {"TITLE": "${{ github.event.pull_request.title }}"}}]
    assert audit(wf(ok, permissions={"contents": "read"})) == []


def test_on_can_be_list_and_bad_input_is_safe():
    steps = [{"uses": f"actions/checkout@{SHA}", "with": {"ref": "${{ github.head_ref }}"}}]
    w = wf(steps, on=["pull_request_target"], permissions={"contents": "read"})
    assert audit(w) == [("build", "PWN_REQUEST")]
    assert audit({}) == [("workflow", "BROAD_PERMISSIONS")]
    assert audit(None) == []
