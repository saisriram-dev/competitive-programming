import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = [0] * (n + 2)
    for x in arr:
        cnt[x] += 1

    spare = 0
    v = 0

    while True:
        if cnt[v] == 0 or spare + cnt[v] < k:
            return v

        spare = spare + cnt[v] - k
        v += 1


t = int(input())
for _ in range(t):
    print(solve())
