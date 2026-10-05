import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    res = []

    for i in range(n):
        greater = 0
        lesser = 0

        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                greater += 1
            elif arr[j] < arr[i]:
                lesser += 1
        
        res.append(max(greater, lesser))

    return res

t = int(input())
for _ in range(t):
    print(*solve())
