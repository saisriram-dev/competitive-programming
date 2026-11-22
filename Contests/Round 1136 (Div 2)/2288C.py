import sys
import math

input = sys.stdin.readline


def solve():
    n, attack = map(int, input().split())
    healths = list(map(int, input().split()))
    healths.sort()

    spell_cards = 0
    hits = [math.ceil(health / attack) for health in healths]
    for j in range(len(hits) - 1):
        hits[j] -= j
        spell_cards = max(spell_cards, hits[j])

    return spell_cards - 1


t = int(input())
for _ in range(t):
    print(solve())
