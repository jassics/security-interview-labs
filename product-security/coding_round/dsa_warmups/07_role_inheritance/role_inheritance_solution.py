"""DS-07 reference solution."""


def effective_permissions(parents, grants, role):
    """All permissions a role has, including those inherited from parent roles.

    parents: dict role -> list of parent roles
    grants:  dict role -> iterable of permissions granted directly
    Unknown roles have no parents and no grants. Cycles are tolerated.
    """
    seen = set()
    permissions = set()
    stack = [role]
    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)
        permissions |= set(grants.get(current, ()))
        stack.extend(parents.get(current, ()))
    return permissions


def has_inheritance_cycle(parents):
    """True if the role inheritance graph contains a cycle (including a role inheriting itself)."""
    state = {}  # missing = unvisited, 1 = on the current path, 2 = finished
    for start in parents:
        if start in state:
            continue
        state[start] = 1
        stack = [(start, iter(parents.get(start, ())))]
        while stack:
            node, children = stack[-1]
            for child in children:
                child_state = state.get(child)
                if child_state == 1:
                    return True
                if child_state is None:
                    state[child] = 1
                    stack.append((child, iter(parents.get(child, ()))))
                    break
            else:
                state[node] = 2
                stack.pop()
    return False
