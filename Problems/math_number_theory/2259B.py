from collections import Counter
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        if arr[i] % 2 != 0:
            arr[i] = 1
        elif arr[i] % 4 == 0:
            arr[i] = 2
        elif arr[i] % 2 == 0 and arr[i] % 4 != 0:
            arr[i] = 0

    counts = Counter(arr)

    return max(counts.values())

t = int(input().strip())
for _ in range(t):
    print(solve())
