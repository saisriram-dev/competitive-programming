import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    prefix_len = n - k + 1
    s = set(arr[:prefix_len])

    # Find missing values from 0 to prefix_len - 1
    missing = []
    for val in range(prefix_len):
        if val not in s:
            missing.append(val)

    if not missing:
        return -1

    # Find an element inside the prefix greater than the missing value to swap out
    max_val = -1
    max_idx = -1
    for i in range(prefix_len):
        if arr[i] > missing[0]:
            if arr[i] > max_val:
                max_val = arr[i]
                max_idx = i

    # Find the position of the missing value outside the prefix
    idx = -1
    for i in range(prefix_len, n):
        if arr[i] == missing[0]:
            idx = i
            break
            
    return f"{max_idx + 1} {idx + 1}"

t = int(input().strip())
for _ in range(t):
    print(solve())
