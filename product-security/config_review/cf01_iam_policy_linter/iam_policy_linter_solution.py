def _as_list(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def lint_policy(policy):
    findings = set()
    statements = _as_list((policy or {}).get("Statement"))
    for index, st in enumerate(statements):
        if not isinstance(st, dict) or st.get("Effect") != "Allow":
            continue
        actions = [str(a).lower() for a in _as_list(st.get("Action"))]
        resources = [str(r) for r in _as_list(st.get("Resource"))]
        all_actions = "*" in actions
        all_resources = "*" in resources

        if all_actions and all_resources:
            findings.add((index, "ADMIN_ALL"))
        else:
            if any(a == "*" or a.endswith(":*") for a in actions):
                findings.add((index, "WILDCARD_ACTION"))
            if all_resources and any(a != "sts:getcalleridentity" for a in actions):
                findings.add((index, "WILDCARD_RESOURCE"))

        principal = st.get("Principal")
        public = principal == "*" or (
            isinstance(principal, dict) and "*" in _as_list(principal.get("AWS"))
        )
        if public and not st.get("Condition"):
            findings.add((index, "PUBLIC_PRINCIPAL"))

        if "iam:passrole" in actions and all_resources:
            findings.add((index, "PASSROLE_WILDCARD"))
        if "NotAction" in st:
            findings.add((index, "NOT_ACTION_ALLOW"))
    return sorted(findings)
