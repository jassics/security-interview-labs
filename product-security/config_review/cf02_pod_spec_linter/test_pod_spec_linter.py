import copy
import importlib
import os

impl = importlib.import_module(os.environ.get("IMPL", "pod_spec_linter_solution"))
lint = impl.lint_manifest

GOOD_CONTAINER = {
    "name": "app",
    "image": "registry.example.com/app:1.4.2",
    "securityContext": {
        "runAsNonRoot": True,
        "allowPrivilegeEscalation": False,
        "capabilities": {"drop": ["ALL"]},
    },
    "resources": {"limits": {"cpu": "500m", "memory": "256Mi"}},
}


def pod(container=None, **spec):
    return {"kind": "Pod", "spec": {"containers": [container or copy.deepcopy(GOOD_CONTAINER)], **spec}}


def test_hardened_pod_has_no_findings():
    assert lint(pod()) == []


def test_privileged_and_root():
    c = copy.deepcopy(GOOD_CONTAINER)
    c["securityContext"] = {"privileged": True, "runAsUser": 0,
                            "allowPrivilegeEscalation": False, "capabilities": {"drop": ["ALL"]}}
    assert lint(pod(c)) == [("app", "PRIVILEGED"), ("app", "RUNS_AS_ROOT")]


def test_pod_level_run_as_non_root_counts():
    c = copy.deepcopy(GOOD_CONTAINER)
    del c["securityContext"]["runAsNonRoot"]
    assert ("app", "RUNS_AS_ROOT") in lint(pod(c))
    assert lint(pod(c, securityContext={"runAsNonRoot": True})) == []


def test_missing_security_context_flags_the_defaults():
    c = {"name": "app", "image": "app:1.0", "resources": {"limits": {"cpu": "1"}}}
    assert lint(pod(c)) == [("app", "CAPS_NOT_DROPPED"), ("app", "PRIV_ESCALATION"), ("app", "RUNS_AS_ROOT")]


def test_mutable_images():
    for image, bad in [("app", True), ("app:latest", True), ("app:1.0", False),
                       ("reg:5000/app", True), ("reg:5000/app:2", False),
                       ("app@sha256:" + "a" * 64, False)]:
        c = copy.deepcopy(GOOD_CONTAINER)
        c["image"] = image
        assert (("app", "MUTABLE_IMAGE") in lint(pod(c))) is bad, image


def test_no_limits():
    c = copy.deepcopy(GOOD_CONTAINER)
    del c["resources"]
    assert lint(pod(c)) == [("app", "NO_LIMITS")]


def test_host_access_and_host_path():
    out = lint(pod(hostNetwork=True, volumes=[{"name": "v", "hostPath": {"path": "/"}}]))
    assert out == [("pod", "HOST_ACCESS"), ("pod", "HOST_PATH")]


def test_deployment_and_init_containers():
    bad = copy.deepcopy(GOOD_CONTAINER)
    bad["name"] = "init"
    bad["securityContext"]["privileged"] = True
    dep = {"kind": "Deployment",
           "spec": {"template": {"spec": {"containers": [copy.deepcopy(GOOD_CONTAINER)],
                                          "initContainers": [bad]}}}}
    assert lint(dep) == [("init", "PRIVILEGED")]


def test_bad_input_does_not_crash():
    assert lint({}) == []
    assert lint(None) == []
    assert lint({"kind": "Pod", "spec": {"containers": ["oops"]}}) == []
