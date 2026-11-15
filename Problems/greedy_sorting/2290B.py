import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    a = str(input().strip())

    c = 0
    for i in range(1, n):
        if a[i] == a[i - 1]:
            c += 1

    if a[0] != "R":
        c += 1

    return c


t = int(input())
for _ in range(t):
    print(solve())
