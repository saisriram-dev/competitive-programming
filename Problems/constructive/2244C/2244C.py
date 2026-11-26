import sys
from math import gcd

input = sys.stdin.readline


def solve():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    g = gcd(x, y)

    for i in range(n):
        if (i + 1) % g != a[i] % g:
            return "NO"

    return "YES"


t = int(input())
for _ in range(t):
    print(solve())
