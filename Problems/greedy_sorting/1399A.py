import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # Sort the array directly (duplicates are handled naturally since diff == 0 <= 1)
    arr.sort()

    for i in range(1, n):
        if arr[i] - arr[i - 1] > 1:
            return "NO"

    return "YES"

t = int(input())
for _ in range(t):
    print(solve())
