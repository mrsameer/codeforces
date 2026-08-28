#!/usr/bin/env python3
"""Codeforces 474A — Keyboard.
https://codeforces.com/problemset/problem/474/A

Hands shifted one key to the R mean every printed character sits one position
right of the one intended, so recovering the text shifts back the other way.
"""
import os
import sys

MOD = 1_000_000_007
INF = float("inf")
IINF = 2 * 10**9

# All of stdin is read on first use, so this template is not suitable for
# interactive problems — those need sys.stdin.readline plus an explicit flush.
_tokens = None


def _next() -> bytes:
    global _tokens
    if _tokens is None:
        _tokens = iter(sys.stdin.buffer.read().split())
    return next(_tokens)


def ni() -> int:
    """Next whitespace-separated token as an int."""
    return int(_next())


def ns() -> str:
    """Next whitespace-separated token as a str."""
    return _next().decode()


def nints(k: int) -> list[int]:
    """Next k tokens as a list of ints."""
    return [int(_next()) for _ in range(k)]


def nstrs(k: int) -> list[str]:
    """Next k tokens as a list of strs."""
    return [_next().decode() for _ in range(k)]


_out: list[str] = []


def emit(*values: object) -> None:
    """Queue one space-joined line of output. Do not mix with print()."""
    _out.append(" ".join(map(str, values)))


def dbg(*values: object) -> None:
    """Print to stderr under `cf run` / `cf test`; a no-op on the judge."""
    if os.environ.get("CF_LOCAL") == "1":
        print("[dbg]", *values, file=sys.stderr)


def solve() -> None:
    direction = ns()
    s = ns()
    keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"

    if (direction == "R"):
        emit("".join(keyboard[keyboard.index(c) - 1] for c in s))
    else:
        emit("".join(keyboard[keyboard.index(c) + 1] for c in s))

def main() -> None:
    solve()


if __name__ == "__main__":
    main()
    sys.stdout.write("\n".join(_out) + ("\n" if _out else ""))
