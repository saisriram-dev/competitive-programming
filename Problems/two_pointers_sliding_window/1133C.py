n = int(input())
arr = list(map(int, input().split()))
arr.sort()

i = 0
j = 0
ans = 0

while j < n:
    if arr[j] - arr[i] <= 5:
        ans = max(ans, j - i + 1)
        j += 1
    else:
        while arr[j] - arr[i] > 5:
            i += 1

print(ans)
