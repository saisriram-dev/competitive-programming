from collections import Counter
import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    counts = Counter(arr)

    if arr[0] == arr[-1] == 0:
        return 0
    elif arr[0] == arr[-1] == 1:
        if counts[0] >= 2:
            return 2
        else:
            return -1
    else:
        if counts[0] >= 2:
            return 1
        else:
            return -1


t = int(input().strip())
for _ in range(t):
    print(solve())
