import sys
input = sys.stdin.readline

def solve():
    x, y, z = map(int, input().split())

    if z >= x:
        return "S" * (x + y + z)
    elif y >= z:
        return "R" * (x + y + z)
    else:
        return "P" * (x + y + z)

t = int(input())
for _ in range(t):
    print(solve())
