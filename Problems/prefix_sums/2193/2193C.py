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

    res = []  
    for query in queries:
        l, r = query
        ans = sum(max_vals[l-1:r])
        res.append(str(ans))

    print(" ".join(res))

t = int(input())
for _ in range(t):
    solve()
