import sys
input = sys.stdin.readline

def solve():
    a = int(input())

    return (10 ** len(str(a))) + 1


t = int(input())
for _ in range(t):
    print(solve())
