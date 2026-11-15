import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    if n < 4:
        return "-1"

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    arr = []
    remaining = []

    for i in range(2, n + 1):
        if not is_prime[i]:
            arr.append(i)
        else:
            remaining.append(i)

    elements = arr + remaining

    elements.insert(3, 1)

    return " ".join(map(str, elements))


t = int(input())
for _ in range(t):
    print(solve())
