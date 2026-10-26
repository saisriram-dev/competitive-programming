import sys
input = sys.stdin.readline

def can(M, cnt, k):
    # Can we build groups with maxima 0, 1, ..., M-1?
    spare = 0
    for v in range(M):
        if cnt[v] == 0:
            return False
        available = spare + cnt[v]
        if available < k:
            return False
        spare = available - k
    return True

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = [0] * (n + 2)
    for x in arr:
        cnt[x] += 1

    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can(mid, cnt, k):
            lo = mid        # mid works, so the answer is at least mid
        else:
            hi = mid - 1    # mid fails, so the answer is below mid
    return lo

t = int(input())
for _ in range(t):
    print(solve())
