import sys

input = sys.stdin.readline


def solve():
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = {}
    res = 0

    for a in arr:
        need = ((-a) % x, a % y)
        res += cnt.get(need, 0)

        key = (a % x, a % y)
        cnt[key] = cnt.get(key, 0) + 1

    return res


t = int(input())
for _ in range(t):
    print(solve())
