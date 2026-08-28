"""Codeforces 4A — Watermelon.  https://codeforces.com/problemset/problem/4/A

A weight w splits into two even positive parts iff w is even and w > 2.
The Python twin of example/watermelon.cpp — same samples, same answers.
"""
import sys


def main() -> None:
    w = int(sys.stdin.buffer.read())
    print("YES" if w % 2 == 0 and w > 2 else "NO")


main()
