import sys
from collections import Counter
from bisect import bisect_right
input = sys.stdin.readline

def solve():
    n, max_height = map(int, input().split())
    heights = list(map(int, input().split()))
    
    heights.sort()
    cnt = Counter(heights)

    candidates = set()
    for v in cnt:
        candidates.add(v)
        if v % 2 == 0:
            candidates.add(v // 2)

    best = 0
    for L in candidates:
        greater = n - bisect_right(heights, L)
        total = cnt.get(L, 0) + greater + cnt.get(2*L, 0)
        if total > best:
            best = total

    return best
    

t = int(input())
for _ in range(t):
    print(solve())
