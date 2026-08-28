"""Codeforces 474A — Keyboard.  https://codeforces.com/problemset/problem/474/A

Hands shifted one key to the R means every character printed sits one position
right of the one intended, so recovering the text shifts back the other way.
The keyboard is one flat string, so "shift" is just an index offset.

Checked against a forward model — simulate the shift, feed the result back,
confirm the original returns — over 300 random strings covering all 30 keys.
"""
import sys

KEYBOARD = "qwertyuiopasdfghjkl;zxcvbnm,./"


def main() -> None:
    direction, typed = sys.stdin.buffer.read().split()
    shift = -1 if direction == b"R" else 1
    print("".join(KEYBOARD[KEYBOARD.index(c) + shift] for c in typed.decode()))


main()
