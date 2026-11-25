#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        long long x, y;
        cin >> n >> x >> y;

        map<pair<long long, long long>, int> cnt;
        long long res = 0;

        for (int i = 0; i < n; i++) {
            long long a;
            cin >> a;

            long long rx = a % x;
            long long ry = a % y;
            long long need_x = (x - rx) % x;

            auto it = cnt.find({need_x, ry});
            if (it != cnt.end()) res += it->second;

            cnt[{rx, ry}]++;
        }

        cout << res << "\n";
    }
    return 0;
}
