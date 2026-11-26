import importlib
import os

impl = importlib.import_module(os.environ.get("IMPL", "iam_policy_linter_solution"))
lint = impl.lint_policy


def policy(*statements):
    return {"Version": "2012-10-17", "Statement": list(statements)}


def test_admin_all():
    p = policy({"Effect": "Allow", "Action": "*", "Resource": "*"})
    assert lint(p) == [(0, "ADMIN_ALL")]


def test_service_wildcard_on_specific_resource():
    p = policy({"Effect": "Allow", "Action": "s3:*", "Resource": "arn:aws:s3:::reports/*"})
    assert lint(p) == [(0, "WILDCARD_ACTION")]


def test_wildcard_resource_with_specific_action():
    p = policy({"Effect": "Allow", "Action": ["ec2:DescribeInstances"], "Resource": "*"})
    assert lint(p) == [(0, "WILDCARD_RESOURCE")]


def test_get_caller_identity_alone_is_fine():
    p = policy({"Effect": "Allow", "Action": "sts:GetCallerIdentity", "Resource": "*"})
    assert lint(p) == []


def test_public_principal_without_condition():
    p = policy({"Effect": "Allow", "Principal": {"AWS": "*"}, "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::b/*"})
    assert lint(p) == [(0, "PUBLIC_PRINCIPAL")]


def test_public_principal_with_condition_is_not_flagged():
    p = policy({"Effect": "Allow", "Principal": "*", "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::b/*",
                "Condition": {"StringEquals": {"aws:SourceVpce": "vpce-123"}}})
    assert lint(p) == []


def test_passrole_wildcard():
    p = policy({"Effect": "Allow", "Action": ["iam:PassRole"], "Resource": "*"})
    assert lint(p) == [(0, "PASSROLE_WILDCARD"), (0, "WILDCARD_RESOURCE")]


def test_not_action_allow():
    p = policy({"Effect": "Allow", "NotAction": "iam:*", "Resource": "arn:aws:s3:::b"})
    assert lint(p) == [(0, "NOT_ACTION_ALLOW")]


def test_deny_is_ignored_and_case_is_ignored():
    p = policy({"Effect": "Deny", "Action": "*", "Resource": "*"},
               {"Effect": "Allow", "Action": "S3:*", "Resource": "arn:aws:s3:::b"})
    assert lint(p) == [(1, "WILDCARD_ACTION")]


def test_single_statement_dict_and_bad_input():
    assert lint({"Statement": {"Effect": "Allow", "Action": "*", "Resource": "*"}}) == [(0, "ADMIN_ALL")]
    assert lint({}) == []
    assert lint(None) == []
    assert lint(policy("not a dict")) == []
