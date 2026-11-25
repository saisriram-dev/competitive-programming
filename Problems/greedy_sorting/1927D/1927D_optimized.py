import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    p = [-1] * n
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            p[i] = i - 1
        else:
            p[i] = p[i - 1]

    res = []
    for l, r in queries:
        l -= 1
        r -= 1

        if p[r] >= l:
            res.append((p[r] + 1, r + 1))
        else:
            res.append((-1, -1))

    return "\n".join(f"{u} {v}" for u, v in res)


t = int(input())
for _ in range(t):
    print(solve())
