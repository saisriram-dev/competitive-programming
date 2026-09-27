import math
import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    arr = list(map(int, input().split()))

    if n == 1:
        return arr[0]

    return math.gcd(arr[0], arr[-1])

t = int(input().strip())
for _ in range(t):
    print(solve())
