import sys

input = sys.stdin.readline


def solve():
    n, k, p = map(int, input().split())
    joy_pts = list(map(int, input().split()))
    joy_pts.sort(reverse=True)

    joy = 0

    while len(joy_pts) >= k:
        c = 0

        for _ in range(k):
            c += joy_pts.pop()

        if c <= p:
            joy += p
        else:
            joy += c
            break

    return joy + sum(joy_pts)


t = int(input())
for _ in range(t):
    print(solve())
