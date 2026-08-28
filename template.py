#!/usr/bin/env python3
"""Codeforces solution template.

Read with the token helpers below (much faster than input()), write with
emit() — output is buffered and flushed once, at exit.
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
    n = ni()
    emit(n)


def main() -> None:
    t = ni()  # delete this line for single-test problems
    for _ in range(t):
        solve()


# Deliberately no sys.setrecursionlimit() here. CPython's default of 1000 is
# low, but raising it costs memory on the judge — under PyPy on Codeforces a
# large limit can trip the memory limit at startup, before main() even runs.
# Prefer an explicit stack; if you truly need recursion, raise the limit inside
# main() to the smallest value that works and submit under CPython.
if __name__ == "__main__":
    main()
    sys.stdout.write("\n".join(_out) + ("\n" if _out else ""))
