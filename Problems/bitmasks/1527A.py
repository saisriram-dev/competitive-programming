import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    count = 0
    curr = 0

    while n:
        curr = n - 1
        n &= curr
        count += 1

    return curr

t = int(input())
for _ in range(t):
    print(solve())
