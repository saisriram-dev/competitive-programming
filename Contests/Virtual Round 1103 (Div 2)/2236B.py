import sys

input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    s = input().strip()

    low = 0
    high = n - k

    allowed = []
    allowed_2 = set()

    for i in range(low, high):
        allowed.append((i, i + k))
        allowed_2.add(i)
        allowed_2.add(i + k)

    # Check positions that cannot be affected
    for i in range(n):
        if i not in allowed_2 and s[i] == "1":
            return "NO"

    # Check parity of each independent chain
    for start in range(k):
        ones = 0
        for j in range(start, n, k):
            if s[j] == "1":
                ones += 1

        if ones % 2 != 0:
            return "NO"

    return "YES"


t = int(input())
for _ in range(t):
    print(solve())
