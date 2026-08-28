"""Codeforces 26A — Almost Prime.
https://codeforces.com/problemset/problem/26/A

A number is almost prime when it has exactly two distinct prime divisors.
Rather than factorizing each number, sieve the divisor counts in one pass:
for every prime p, walk its multiples and bump their counter.

The sieve is the smallest_prime_factors idea from snippets/py/number_theory.py,
adapted to count distinct primes instead of recording the least one.
"""
import sys


def main() -> None:
    n = int(sys.stdin.buffer.read())
    distinct = [0] * (n + 1)
    for p in range(2, n + 1):
        if distinct[p] == 0:  # p is prime — nothing smaller divided it
            for multiple in range(p, n + 1, p):
                distinct[multiple] += 1
    print(sum(1 for x in range(2, n + 1) if distinct[x] == 2))


main()
