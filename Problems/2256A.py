import sys
input = sys.stdin.readline

def solve():
    arr = list(map(int, input().split()))
    arr.sort()

    diff = arr[2] - arr[0]

    if diff < (arr[2] + arr[1]) - arr[2]:
        return diff
    else:
        return (arr[2] + arr[1]) - arr[2]


t = int(input())
for _ in range(t):
    print(solve())
