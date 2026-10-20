import sys
input = sys.stdin.readline

def get_mex(subarr):
    subarr = set(subarr)
    mex = 0
    while mex in subarr:
        mex += 1
    return mex

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    max_mex = 0

    for i in range(2 * n):
        l, r = i, i
        while l >= 0 and r < 2 * n and arr[l] == arr[r]:
            max_mex = max(max_mex, get_mex(arr[l: r + 1]))
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < 2 * n and arr[l] == arr[r]:
            max_mex = max(max_mex, get_mex(arr[l: r + 1]))
            l -= 1
            r += 1

    return max_mex

t = int(input())
for _ in range(t):
    print(solve())
