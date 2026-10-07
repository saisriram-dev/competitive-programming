import sys
input = sys.stdin.readline

def solve():
    xo, yo, r = map(int, input().split())
    x = xo
    y = r + yo
    return f"{x} {y}"

t = int(input())
for _ in range(t):
    print(solve())
