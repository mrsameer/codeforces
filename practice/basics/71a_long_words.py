"""Codeforces 71A — Way Too Long Words.
https://codeforces.com/problemset/problem/71/A

Words longer than 10 characters become first + (length - 2) + last.
Shows the read-all / join-once output pattern from template.py.
"""
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    out = []
    for word in data[1 : n + 1]:
        w = word.decode()
        out.append(w if len(w) <= 10 else f"{w[0]}{len(w) - 2}{w[-1]}")
    sys.stdout.write("\n".join(out) + "\n")


main()
