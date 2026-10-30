import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    non_zeros = [idx for idx, val in enumerate(arr) if val != 0]

    if not non_zeros:
        return " ".join(map(str, arr))

    first = non_zeros[0]
    last = non_zeros[-1]

    arr[first] = 1
    arr[last] = 1

    for i in range(first + 1, last):
        if arr[i] == -1:
            arr[i] = 0

    return " ".join(map(str, arr))

t = int(input())
for _ in range(t):
    print(solve())
