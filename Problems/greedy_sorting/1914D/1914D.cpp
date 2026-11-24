#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> max3(vector<int> arr) {
    vector<pair<int, int>> top;

    for (int i = 0; i < 3; i++) {
        int m = *max_element(arr.begin(), arr.end());
        int idx = max_element(arr.begin(), arr.end()) - arr.begin();

        top.push_back({m, idx});
        arr[idx] = -1; // Mark as used
    }

    return top;
}

void solve() {
    int n;
    cin >> n;

    vector<int> a(n), b(n), c(n);

    for (int &x : a) cin >> x;
    for (int &x : b) cin >> x;
    for (int &x : c) cin >> x;

    vector<pair<int, int>> top3_a = max3(a);
    vector<pair<int, int>> top3_b = max3(b);
    vector<pair<int, int>> top3_c = max3(c);

    int best = 0;

    for (auto [va, ia] : top3_a) {
        for (auto [vb, ib] : top3_b) {
            if (ia == ib) continue;

            for (auto [vc, ic] : top3_c) {
                if (ic == ia || ic == ib) continue;

                best = max(best, va + vb + vc);
            }
        }
    }

    cout << best << '\n';
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
