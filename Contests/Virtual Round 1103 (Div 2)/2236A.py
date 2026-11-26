import sys
import math

input = sys.stdin.readline


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    return (max(a) + 1) - min(a)


t = int(input())
for _ in range(t):
    print(solve())
