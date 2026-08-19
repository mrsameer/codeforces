// Sieve, factorization, gcd-family and fast modular exponentiation.
#pragma once
#include <cstdint>
#include <vector>

// Smallest prime factor sieve; spf[x] factorizes any x <= n in O(log x).
inline std::vector<int> smallest_prime_factors(int n) {
    std::vector<int> spf(n + 1);
    for (int i = 2; i <= n; ++i) {
        if (spf[i] == 0)
            for (std::int64_t j = i; j <= n; j += i)
                if (spf[j] == 0) spf[j] = i;
    }
    return spf;
}

inline std::vector<int> primes_up_to(int n) {
    std::vector<bool> is_prime(n + 1, true);
    std::vector<int> primes;
    for (int i = 2; i <= n; ++i) {
        if (!is_prime[i]) continue;
        primes.push_back(i);
        for (std::int64_t j = (std::int64_t)i * i; j <= n; j += i) is_prime[j] = false;
    }
    return primes;
}

// Trial division; fine up to ~1e12.
inline std::vector<std::pair<std::int64_t, int>> factorize(std::int64_t x) {
    std::vector<std::pair<std::int64_t, int>> factors;
    for (std::int64_t p = 2; p * p <= x; ++p) {
        if (x % p) continue;
        int exp = 0;
        while (x % p == 0) { x /= p; ++exp; }
        factors.push_back({p, exp});
    }
    if (x > 1) factors.push_back({x, 1});
    return factors;
}

inline std::int64_t power_mod(std::int64_t base, std::int64_t exp, std::int64_t mod) {
    std::int64_t result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) result = result * base % mod;
        base = base * base % mod;
        exp >>= 1;
    }
    return result;
}

// Extended Euclid: returns g = gcd(a, b) with a*x + b*y = g.
inline std::int64_t extended_gcd(std::int64_t a, std::int64_t b,
                                 std::int64_t& x, std::int64_t& y) {
    if (b == 0) { x = 1; y = 0; return a; }
    std::int64_t x1, y1;
    std::int64_t g = extended_gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}
