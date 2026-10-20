import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # pref1: 1 -> +1, (2 or 3) -> -1   (left part score)
    # pref2: (1 or 2) -> +1, 3 -> -1   (middle part score)
    pref1 = [0] * (n + 1)
    pref2 = [0] * (n + 1)
    for i in range(1, n + 1):
        v = a[i - 1]
        pref1[i] = pref1[i - 1] + (1 if v == 1 else -1)
        pref2[i] = pref2[i - 1] + (-1 if v == 3 else 1)

    INF = float('inf')
    best = INF
    
    for y in range(2, n):
        x = y - 1
        if pref1[x] >= 0:
            best = min(best, pref2[x])
        if best <= pref2[y]:
            return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    print(solve())
