import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr_set = set(arr)

    for mask in range(1, 1024):
        if all((num ^ mask) in arr_set for num in arr):
            return mask

    return -1

t = int(input())
for _ in range(t):
    print(solve())
