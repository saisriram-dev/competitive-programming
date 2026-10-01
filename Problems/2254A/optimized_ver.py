import sys
input = sys.stdin.readline

def solve():
    arr = list(map(int, input().split()))
    arr.sort()

    return min(arr[1] - arr[0], arr[2] - arr[1])
    
t = int(input())
for _ in range(t):
    print(solve())
