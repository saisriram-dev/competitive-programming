import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        j = i
        count = 0

        while j < n:
            count += arr[j]
            j += arr[j]

        ans = max(ans, count)

    return ans


t = int(input())
for _ in range(t):
    print(solve())
