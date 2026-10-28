import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    r1 = str(input().strip())
    r2 = str(input().strip())

    return (r1.count('f') + r2.count('f')) % 2

t = int(input().strip())
for _ in range(t):
    print(solve())
