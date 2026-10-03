import sys
import math
input = sys.stdin.readline

def solve():
    a, b = map(int, input().split())

    z = a / b

    if math.floor(z) == z:
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    print(solve())
