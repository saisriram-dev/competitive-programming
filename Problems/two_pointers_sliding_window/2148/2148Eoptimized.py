import sys
input = sys.stdin.readline
from collections import Counter

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    total = [0] * (n + 1)
    for num in a:
        total[num] += 1

    for c in total:
        if c % k != 0:
            return 0

    lim = [c // k for c in total]
    cur = [0] * (n + 1)

    l = 0
    ans = 0
    for r in range(n):
        x = a[r]
        cur[x] += 1

        while cur[x] > lim[x]:
            cur[a[l]] -= 1
            l += 1

        ans += r - l + 1

    return ans


t = int(input())
for _ in range(t):
    print(solve())
