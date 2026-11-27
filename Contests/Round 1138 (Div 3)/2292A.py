import sys

input = sys.stdin.readline


def solve():
    l, a, b = map(int, input().split())
    a_positions = set()
    b_positions = set()

    i = 0
    while True:
        val = (i * a) % l

        if val in a_positions:
            break

        a_positions.add(val)
        i += 1

    i = 0
    while True:
        val = (i * b) % l

        if val in b_positions:
            break

        b_positions.add(val)
        i += 1

    greater = 1 if len(a_positions) >= len(b_positions) else 0
    ans = 0

    if greater == 1:
        for num in b_positions:
            if num in a_positions:
                ans += 1
    else:
        for num in a_positions:
            if num in b_positions:
                ans += 1

    return ans


t = int(input())
for _ in range(t):
    print(solve())
