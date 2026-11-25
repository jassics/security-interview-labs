"""Template for stdin/stdout judges (HackerRank, HackerEarth and similar).

Example input:
    3
    1 2 3
Example output:
    6

Read the problem's input format carefully and change main() to match it.
"""
import sys


def solve(numbers):
    """Keep the real logic in a pure function so you can test it without stdin."""
    return sum(numbers)


def main():
    data = sys.stdin.read().split()  # reads everything at once; fast for large input
    n = int(data[0])
    numbers = [int(token) for token in data[1:1 + n]]
    print(solve(numbers))


if __name__ == "__main__":
    main()
