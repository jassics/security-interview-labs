# Coding round

Three kinds of practice, because security coding rounds ask for all three.

| Folder | What it is |
| --- | --- |
| `tier1_bruteforce_detector/` | Security-flavoured scripting problem (CR-01) with a longer write-up |
| `dsa_warmups/` | Basic to medium algorithm problems in the style of LeetCode, HackerRank and HackerEarth, with security framing (DS-01 to DS-08) |
| `platform_templates/` | Starting points for stdin/stdout judges, plus a checklist for practising |
| `CHEATSHEET.md` | Python and Java syntax you are likely to forget |

## Why basic algorithm problems belong here

For many security engineering roles the coding round is not a hard algorithms test. It checks that you can read a problem, write correct code, run it and handle edge cases, often on an online judge. The warm-ups train exactly that, using problems that also teach a security idea (replay, parser differentials, denial of service through input shape, privilege windows, permission graphs).

The suggested times are practice targets, not requirements from any company.

## Warm-up problems

| ID | Problem | Pattern | Level | Security idea |
| --- | --- | --- | --- | --- |
| DS-01 | First replayed nonce | Hash set | Easy | Replay attacks |
| DS-02 | Balanced template braces | Stack | Easy | Input shape as denial of service |
| DS-03 | Strict IPv4 validator | String parsing, edge cases | Easy | Parser differentials, SSRF filter bypass |
| DS-04 | Top K noisiest IPs | Counting, sort or heap | Easy to medium | Log analysis at scale |
| DS-05 | Merge access windows | Intervals | Medium | Continuous privileged access |
| DS-06 | Longest window with at most K distinct IPs | Sliding window | Medium | Bot and scanner signals |
| DS-07 | Role inheritance and cycles | Graph, cycle detection | Medium | Authorization data as an attack surface |
| DS-08 | First vulnerable version | Binary search | Medium | Bisecting regressions and CVE windows |

Every problem has a stub to fill in, a reference solution, tests, hints and a "what the interviewer listens for" section. Practise like this:

```bash
cd product-security
# write your solution in coding_round/dsa_warmups/01_first_replayed_nonce/first_replayed_nonce.py
IMPL=first_replayed_nonce pytest coding_round/dsa_warmups/01_first_replayed_nonce
```

Run the whole folder against the reference solutions with `make test-python`.

## Planned next

More patterns at the same level: two pointers, prefix sums, heaps and priority queues, tries (URL and path allowlists), union-find, string and regex tasks, basic dynamic programming. Security-scripting problems (log parsers, secret scanners, JWT checks, IAM policy analysers) continue as tier 1 to 3.
