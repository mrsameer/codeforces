// Compile-time modular arithmetic. Default modulus is 1e9+7.
#pragma once
#include <cstdint>
#include <iostream>

template <std::int64_t MOD = 1'000'000'007LL>
struct ModInt {
    std::int64_t v;

    ModInt(std::int64_t x = 0) : v(((x % MOD) + MOD) % MOD) {}

    ModInt& operator+=(const ModInt& o) { if ((v += o.v) >= MOD) v -= MOD; return *this; }
    ModInt& operator-=(const ModInt& o) { if ((v -= o.v) < 0) v += MOD; return *this; }
    ModInt& operator*=(const ModInt& o) { v = v * o.v % MOD; return *this; }
    ModInt& operator/=(const ModInt& o) { return *this *= o.inv(); }

    friend ModInt operator+(ModInt a, const ModInt& b) { return a += b; }
    friend ModInt operator-(ModInt a, const ModInt& b) { return a -= b; }
    friend ModInt operator*(ModInt a, const ModInt& b) { return a *= b; }
    friend ModInt operator/(ModInt a, const ModInt& b) { return a /= b; }
    friend bool operator==(const ModInt& a, const ModInt& b) { return a.v == b.v; }

    // Fast exponentiation; also the basis of inv() via Fermat's little theorem.
    ModInt pow(std::int64_t e) const {
        ModInt base = *this, result = 1;
        while (e > 0) {
            if (e & 1) result *= base;
            base *= base;
            e >>= 1;
        }
        return result;
    }

    // Valid only for prime MOD, which holds for the usual 1e9+7 / 998244353.
    ModInt inv() const { return pow(MOD - 2); }

    friend std::ostream& operator<<(std::ostream& os, const ModInt& m) { return os << m.v; }
    friend std::istream& operator>>(std::istream& is, ModInt& m) {
        std::int64_t x; is >> x; m = ModInt(x); return is;
    }
};

using mint = ModInt<1'000'000'007LL>;
using mint998 = ModInt<998'244'353LL>;
