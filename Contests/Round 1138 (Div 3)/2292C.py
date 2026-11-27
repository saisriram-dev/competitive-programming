import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    s = str(input().strip())

    if len(s) % 2 != 0:
        return "NO"

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            return "YES"

    return "NO"


t = int(input())
for _ in range(t):
    print(solve())
