# DS-07: Role inheritance and cycles

**Pattern:** graph traversal and cycle detection · **Difficulty:** medium · **Suggested time:** 25 to 30 minutes · **Language:** Python

## Problem

An access system lets a role inherit from parent roles. You get two dictionaries: `parents` (role to list of parent roles) and `grants` (role to the permissions it gets directly).

Write two functions:

1. `effective_permissions(parents, grants, role)`: every permission the role has, directly or through any chain of parents. Unknown roles have no parents and no grants. The function must **terminate even if the data contains a cycle**.
2. `has_inheritance_cycle(parents)`: `True` if any role ends up inheriting from itself.

```python
parents = {"admin": ["editor"], "editor": ["viewer"], "viewer": []}
grants = {"admin": {"delete"}, "editor": {"write"}, "viewer": {"read"}}
effective_permissions(parents, grants, "admin")  # {"delete", "write", "read"}
has_inheritance_cycle({"a": ["b"], "b": ["a"]})    # True
```

## How to practise

Write both functions in `role_inheritance.py`, then run `IMPL=role_inheritance pytest coding_round/dsa_warmups/07_role_inheritance`.

## Hints

<details>
<summary>Hint 1: permissions</summary>

This is reachability: walk from the role to everything it can reach. What stops you from looping forever?
</details>

<details>
<summary>Hint 2: cycles</summary>

Track which roles are on the path you are currently exploring, separately from roles you have finished. Meeting a role that is on the current path means a cycle.
</details>

<details>
<summary>Hint 3: depth</summary>

The last test has a chain of 50,000 roles. Recursive depth-first search will hit Python's recursion limit. Use an explicit stack.
</details>

## What the interviewer listens for

- You say "graph" and name BFS or DFS, and you explain that a visited set is what makes the first function terminate.
- You distinguish "seen before" (fine in a diamond shape) from "currently on my path" (a cycle). A solution that flags every revisit is wrong for diamonds.
- You mention recursion depth and use an explicit stack when the input is untrusted.
- Security angle: permission graphs are data that people edit. They contain cycles, dangling parents and huge chains. A function that hangs or crashes on them is a denial-of-service bug in the authorization path. This is also the shape of IAM role chaining and group nesting questions.

## Complexity

Both are O(V + E) time and O(V) space. Classic pattern names: "graph reachability" and "course schedule" (cycle detection).
