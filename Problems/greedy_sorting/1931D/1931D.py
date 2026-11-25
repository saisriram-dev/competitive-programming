import sys

input = sys.stdin.readline


def solve():
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))

    vals = [[] for _ in range(n - 1)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            vals[i].append((abs(arr[i] + arr[j]), abs(arr[i] - arr[j])))

    res = 0

    for i in range(len(vals)):
        for u, v in vals[i]:
            if u % x == 0 and v % y == 0:
                res += 1

    return res


t = int(input())
for _ in range(t):
    print(solve())
