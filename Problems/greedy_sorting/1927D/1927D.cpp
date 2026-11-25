#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int q;
    cin >> q;

    vector<pair<int, int>> queries(q);
    for (int i = 0; i < q; i++) {
        cin >> queries[i].first >> queries[i].second;
    }

    vector<int> p(n, -1);

    for (int i = 1; i < n; i++) {
        if (arr[i] != arr[i - 1]) {
            p[i] = i - 1;
        } else {
            p[i] = p[i - 1];
        }
    }

    for (auto [l, r] : queries) {
        l--;
        r--;

        if (p[r] >= l) {
            cout << p[r] + 1 << " " << r + 1 << '\n';
        } else {
            cout << -1 << " " << -1 << '\n';
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}
