"""Codeforces 158A — Next Round.  https://codeforces.com/problemset/problem/158/A

Scores arrive in non-increasing order. A contestant advances with a positive
score that is at least the k-th place score, so the answer is a plain count —
no sorting needed.
"""
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    scores = [int(x) for x in data[2 : 2 + n]]
    cutoff = scores[k - 1]
    print(sum(1 for s in scores if s >= cutoff and s > 0))


main()
