# Coding round cheat sheet: Python and Java

For people who read code more often than they write it. Every line here is something that is easy to forget under pressure.

## Python

```python
# input
import sys
data = sys.stdin.read().split()
n = int(data[0])

# collections
from collections import Counter, defaultdict, deque
counts = Counter(items)              # counts.most_common(3)
groups = defaultdict(list)           # groups[key].append(x)
queue = deque([start])               # queue.popleft(), queue.append(x)

# sorting
sorted(items, key=lambda x: (-x.score, x.name))   # score desc, name asc
items.sort(reverse=True)

# heap (min-heap)
import heapq
heap = []; heapq.heappush(heap, (priority, item)); heapq.heappop(heap)
heapq.nlargest(k, items)

# binary search on a sorted list
import bisect
bisect.bisect_left(sorted_list, x)

# strings
s.split(","), ",".join(parts), s.strip(), s.startswith("x")
s[::-1]                      # reversed copy
ord("a"), chr(97)

# sets and dicts
a & b, a | b, a - b          # intersection, union, difference
d.get(key, default), d.setdefault(key, []), list(d.items())

# loops
for i, x in enumerate(items): ...
for a, b in zip(xs, ys): ...
any(cond(x) for x in xs), all(cond(x) for x in xs)

# safe building blocks for security tasks
import re, json, hashlib, hmac, ipaddress
re.fullmatch(r"[a-z0-9_]{1,32}", s)
hmac.compare_digest(a, b)    # constant-time compare
subprocess.run(["cmd", arg], capture_output=True, text=True)  # no shell=True
```

## Java

```java
// collections
Map<String, Integer> counts = new HashMap<>();
counts.merge(key, 1, Integer::sum);
List<Integer> list = new ArrayList<>();
Deque<Integer> stack = new ArrayDeque<>();     // push, pop, peek
Queue<Integer> queue = new ArrayDeque<>();     // offer, poll
Set<String> seen = new HashSet<>();            // seen.add(x) returns false if already there
PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);

// sorting
Arrays.sort(array);
list.sort(Comparator.comparing(Item::score).reversed().thenComparing(Item::name));

// strings
StringBuilder sb = new StringBuilder(); sb.append(x); sb.toString();
s.split("\\s+"), s.trim(), s.toCharArray(), String.join(",", parts)

// safety
// compare long values with equals or ==, never == on boxed Integer above 127
// beware (low + high) overflow: use low + (high - low) / 2
```

## Habits that score points

- Restate the problem and ask about limits before you code.
- Write the simple version first and say its complexity, then improve it.
- Name edge cases aloud: empty, one element, duplicates, huge input, malformed input.
- Run the code on the sample, then on an edge case you chose.
