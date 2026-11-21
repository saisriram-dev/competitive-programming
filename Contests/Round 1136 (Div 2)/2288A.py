import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    best = float("inf")
    c = 0

    while c + 1 < best:
        power = c + 1
        rem = n
        attacks = 0

        while rem > 0 and power > 0:
            rem -= power
            power -= 1
            attacks += 1

        if rem <= 0:
            best = min(best, c + attacks)
        c += 1

    return best


t = int(input())
for _ in range(t):
    print(solve())
