import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    ans = 0

    for i in range(n, 0, -1):
        final = i ^ (i - 1)
        ans += final.bit_count()

    return ans


t = int(input())
for _ in range(t):
    print(solve())
