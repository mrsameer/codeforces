#include <bits/stdc++.h>
using namespace std;

using ll  = long long;
using ull = unsigned long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

#define all(x)  (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define sz(x)   ((int)(x).size())

// [[maybe_unused]] keeps -Wextra quiet on problems that need only some of these.
[[maybe_unused]] constexpr ll  MOD  = 1'000'000'007LL;
[[maybe_unused]] constexpr ll  INF  = (ll)4e18;
[[maybe_unused]] constexpr int IINF = (int)2e9;

#ifdef LOCAL
#define dbg(...) cerr << "[" << #__VA_ARGS__ << "] = ", dbg_out(__VA_ARGS__)
template <typename T>
void dbg_out(const T& x) { cerr << x << '\n'; }
template <typename T, typename... R>
void dbg_out(const T& x, const R&... rest) { cerr << x << ", ", dbg_out(rest...); }
#else
#define dbg(...)
#endif

void solve() {
    int n;
    cin >> n;
    cout << n << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;          // comment out for single-test problems
    while (t--) solve();
    return 0;
}
