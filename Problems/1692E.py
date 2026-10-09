import sys
input = sys.stdin.readline

def solve():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    total = sum(arr)
    if total < s:
        return -1
    if total == s:
        return 0

    curr = 0
    max_len = -1
    left = 0
    for right in range(n):
        curr += arr[right]

        while curr > s and left <= right:
            curr -= arr[left]
            left += 1

        if curr == s:
            max_len = max(max_len, right - left + 1)

    if max_len == -1:
        return -1
    else:
        return n - max_len
    

t = int(input())
for _ in range(t):
    print(solve())
