import sys
input = sys.stdin.readline

def solve():
    a, b = map(int, input().split())
    if a <= b:
        return -1
    return min(b, a - b)

t = int(input())
for _ in range(t):
    print(solve())
