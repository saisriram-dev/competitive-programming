import sys

input = sys.stdin.readline


def solve():
    a = list(map(int, input().split()))
    a.sort()

    if a[1] - a[0] == a[-1] - a[-2] == 1:
        return "YES"
    else:
        return "NO"


t = int(input())
for _ in range(t):
    print(solve())
