import sys
input = sys.stdin.readline
from collections import Counter

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    freq = Counter(arr)

    for key in freq:
        if freq[key] % k != 0:
            return 0
        freq[key] //= k

    count = 0
    for l in range(n):
        cur = Counter()
        for r in range(l, n):
            cur[arr[r]] += 1
            if cur[arr[r]] > freq[arr[r]]:
                break
            count += 1
    return count

t = int(input())
for _ in range(t):
    print(solve())
