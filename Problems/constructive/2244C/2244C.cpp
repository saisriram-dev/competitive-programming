#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, x, y;
        cin >> n >> x >> y;

        vector<int> p(n);
        for (int i = 0; i < n; i++) cin >> p[i];

        int g = __gcd(x, y);

        bool ok = true;
        for (int i = 0; i < n; i++) {
            // position is i + 1 (1-indexed), value is p[i]
            if ((i + 1) % g != p[i] % g) {
                ok = false;
                break;
            }
        }

        cout << (ok ? "YES" : "NO") << "\n";
    }

    return 0;
}
