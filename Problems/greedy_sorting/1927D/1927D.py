import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    res = []

    for l, r in queries:
        for i in range(l - 1, r - 1):
            if arr[i] != arr[i + 1]:
                res.append((i + 1, i + 2))
                break
            elif i == r - 2:
                res.append((-1, -1))

    return "\n".join(f"{l} {r}" for l, r in res)


t = int(input())
for _ in range(t):
    print(solve())
