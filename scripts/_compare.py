"""Render an expected-vs-actual comparison for cf test.

Reads the expected output file and the actual output, prints a line-aligned
table highlighting mismatches. Exits 0 when they match, 1 otherwise.
"""
import sys

MAX_ROWS = 25
MAX_CELL = 32


def norm(text: str) -> list[str]:
    """Split into lines, dropping trailing whitespace and trailing blank lines."""
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return lines


def cell(value: str | None) -> str:
    if value is None:
        return "\033[2m(nothing)\033[0m"
    if value == "":
        return "\033[2m(empty line)\033[0m"
    return value if len(value) <= MAX_CELL else value[: MAX_CELL - 1] + "…"


def width(value: str | None) -> int:
    if value is None:
        return len("(nothing)")
    if value == "":
        return len("(empty line)")
    return min(len(value), MAX_CELL)


def main() -> int:
    expected_path, actual_path, label = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(expected_path) as f:
        expected = norm(f.read())
    with open(actual_path) as f:
        actual = norm(f.read())

    if expected == actual:
        print(f"\033[32m✓\033[0m {label}")
        return 0

    print(f"\033[31m✗\033[0m {label}")

    first = next(
        (i for i in range(max(len(expected), len(actual)))
         if (expected[i] if i < len(expected) else None)
         != (actual[i] if i < len(actual) else None)),
        0,
    )
    print(f"\n    First difference on line {first + 1}:")
    print(f"        expected: {cell(expected[first] if first < len(expected) else None)}")
    print(f"        you gave: {cell(actual[first] if first < len(actual) else None)}")

    if len(expected) != len(actual):
        print(
            f"\n    \033[33mLine count differs\033[0m — expected {len(expected)}, "
            f"you printed {len(actual)}."
        )
        if len(expected) == len(actual) + 1:
            print("    An extra line in the .out file is the usual cause "
                  "(e.g. the test count pasted in by mistake).")

    total = max(len(expected), len(actual))
    exp_w = max([width(e) for e in expected] + [len("expected")])
    print(f"\n    {'':3} {'line':>4}  {'expected'.ljust(exp_w)}  your output")
    print(f"    {'':3} {'─' * 4}  {'─' * exp_w}  {'─' * 11}")

    shown = 0
    for i in range(total):
        e = expected[i] if i < len(expected) else None
        a = actual[i] if i < len(actual) else None
        ok = e == a
        if shown >= MAX_ROWS:
            print(f"    … {total - i} more line(s) not shown")
            break
        mark = "\033[32m✓\033[0m" if ok else "\033[31m✗\033[0m"
        pad = " " * max(0, exp_w - width(e))
        print(f"    {mark:3} {i + 1:>4}  {cell(e)}{pad}  {cell(a)}")
        shown += 1
    print()
    return 1


if __name__ == "__main__":
    sys.exit(main())
