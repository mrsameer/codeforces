"""Sieves, factorization, extended gcd and modular binomials.

Python has arbitrary-precision ints and a three-argument pow(), so there is no
need for a modint type — use pow(base, exp, MOD) directly.
"""

MOD = 1_000_000_007


def smallest_prime_factors(n: int) -> list[int]:
    """spf[x] is the least prime dividing x; factorizes any x <= n in O(log x)."""
    spf = list(range(n + 1))
    i = 2
    while i * i <= n:
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf


def primes_up_to(n: int) -> list[int]:
    """Sieve of Eratosthenes over a bytearray."""
    if n < 2:
        return []
    is_prime = bytearray([1]) * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            is_prime[i * i:: i] = bytearray(len(range(i * i, n + 1, i)))
    return [i for i in range(2, n + 1) if is_prime[i]]


def factorize(x: int) -> list[tuple[int, int]]:
    """Trial division into (prime, exponent) pairs; fine up to ~1e12."""
    factors = []
    p = 2
    while p * p <= x:
        if x % p == 0:
            exp = 0
            while x % p == 0:
                x //= p
                exp += 1
            factors.append((p, exp))
        p += 1
    if x > 1:
        factors.append((x, 1))
    return factors


def divisors(x: int) -> list[int]:
    """All divisors of x, unsorted, in O(sqrt(x))."""
    small, large = [], []
    d = 1
    while d * d <= x:
        if x % d == 0:
            small.append(d)
            if d != x // d:
                large.append(x // d)
        d += 1
    return small + large[::-1]


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Returns (g, x, y) with a*x + b*y == g == gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


class Binomial:
    """Factorial tables for nCr / nPr modulo a prime.

        binom = Binomial(200_000)
        binom.choose(10, 3)
    """

    def __init__(self, n: int, mod: int = MOD) -> None:
        self.mod = mod
        self.fact = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fact[i] = self.fact[i - 1] * i % mod
        self.inv_fact = [1] * (n + 1)
        self.inv_fact[n] = pow(self.fact[n], mod - 2, mod)
        for i in range(n, 0, -1):
            self.inv_fact[i - 1] = self.inv_fact[i] * i % mod

    def choose(self, n: int, r: int) -> int:
        if r < 0 or r > n:
            return 0
        return self.fact[n] * self.inv_fact[r] % self.mod * self.inv_fact[n - r] % self.mod

    def permute(self, n: int, r: int) -> int:
        if r < 0 or r > n:
            return 0
        return self.fact[n] * self.inv_fact[n - r] % self.mod
