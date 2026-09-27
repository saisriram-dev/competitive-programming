import sys
import math
input = sys.stdin.readline

def solve():
    n, x = map(int, input().split())
    piles = list(map(int, input().split()))
    divisors = []

    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(x // i)
    
    # Don't forget x itself if x > 1
    if x > 1:
        divisors.append(x)

    divisors = list(set(divisors))
    gcds = [(math.gcd(pile, x), pile) for pile in piles]
    max_coins = 0

    for d in divisors:
        curr = 0
        for g, p in gcds:
            if g % d == 0:
                curr += p
        max_coins = max(curr, max_coins)

    return max_coins

t = int(input().strip())
for _ in range(t):
    print(solve())
