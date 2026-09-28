import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # Sort the array directly (duplicates are handled naturally since diff == 0 <= 1)
    arr.sort()
    min_diff = float('inf')

    for i in range(1, n):
        # No need of abs as the array is already sorted
        diff = abs(arr[i] - arr[i - 1])
        min_diff = min(diff, min_diff)

    return min_diff

    
t = int(input())
for _ in range(t):
    print(solve())
