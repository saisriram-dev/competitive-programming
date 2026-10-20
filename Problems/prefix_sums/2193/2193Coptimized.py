import sys
input = sys.stdin.readline

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    queries = []
    for _ in range(q):
        l, r = map(int, input().split())
        queries.append((l, r))
        
    max_vals = [0] * n
    curr_max = 0
    for i in range(n - 1, -1, -1):
        curr_max = max(curr_max, a[i], b[i])
        max_vals[i] = curr_max

    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + max_vals[i]

    res = []
    for _ in range(q):
        l, r = map(int, input().split())
        ans = pref[r] - pref[l - 1]
        res.append(str(ans))

    return " ".join(res)
    
t = int(input())
for _ in range(t):
    solve()
