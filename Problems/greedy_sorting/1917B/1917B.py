import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    s = str(input().strip())

    seen = set()
    total = 0

    for char in s:
        seen.add(char)
        total += len(seen)

    return total


t = int(input())
for _ in range(t):
    print(solve())
