import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    if max(arr) == 1:
        return -1
    elif any(x >= 2 for x in arr[1: n - 1]):
        return sum(arr) - 1
    else:
        return arr[0] + arr[-1] - 1

t = int(input())
for _ in range(t):
    print(solve())
