// Codeforces 4A — Watermelon.
// A weight w splits into two even positive parts iff w is even and w > 2.
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int w;
    cin >> w;
    cout << (w % 2 == 0 && w > 2 ? "YES" : "NO") << '\n';
    return 0;
}
