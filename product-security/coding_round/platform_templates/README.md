# Judge templates

Many online judges (HackerRank, HackerEarth, CodeSignal and similar) and some company coding rounds run your program against hidden inputs. This folder gives you a starting point for the two common styles.

## The two common styles

| Style | You write | Input and output |
| --- | --- | --- |
| **stdin/stdout** (typical for HackerRank and HackerEarth) | A whole program | Read from standard input, print to standard output, in the exact format the problem states |
| **Function signature** (typical for LeetCode) | One function or method, often inside a `Solution` class | The platform calls your function; usually no input parsing at all |

Platforms differ and change over time, so always read the instructions on the page and in your interview invitation.

## Templates

- `stdin_template.py`: Python. Run `python3 stdin_template.py` and type `3` then `1 2 3`, or pipe input in.
- `StdinTemplate.java`: Java 11 or newer. `javac StdinTemplate.java && echo "3 1 2 3" | java StdinTemplate`.
- `test_stdin_template.py`: shows how to test a stdin program with `subprocess`.

The warm-up problems in `../dsa_warmups/` use the function-signature style so they are easy to test. To practise the stdin style, take any of them, keep `solve()` pure, and wrap it in a `main()` like the template.

## Checklist before you submit

1. Run the sample input from the problem statement, not only your own.
2. Print exactly what is asked: no extra text, no debug lines, the right separator and trailing newline.
3. Think about the biggest input. A solution that is fine for 100 items may time out for 10^5.
4. Read input fast: in Python use `sys.stdin.read().split()`; in Java read all bytes or use a `BufferedReader`.
5. Handle empty and one-element inputs.
6. Know the language version on the judge (for example, which Python features exist).
7. State complexity out loud when you finish, even if nobody asks.

## Practise as an interview, not as a puzzle

- Talk before you type: restate the problem, ask about limits and edge cases, outline your approach.
- Write working code first, then improve it.
- Run it. In a live round, running your own tests is part of the answer.
- If you are allowed to use the standard library, say what you are using and why.
- Rules on notes, autocomplete and AI assistants differ by company. Ask the recruiter beforehand; do not assume.
