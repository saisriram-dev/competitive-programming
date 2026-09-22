import sys
input = sys.stdin.readline

def solve():
    piles = list(map(int, input().split()))
    initial = abs(piles[0] - piles[1])

    if piles[1] > piles[0]:
        comp = piles[0] + piles[2]
        if abs(comp - piles[1]) > initial:
            return abs(comp - piles[1])
        else:
            return initial
    else:
        return abs((piles[0] + piles[2]) - piles[1])


n = int(input())             # first line: how many words follow
for _ in range(n):
    print(solve())
