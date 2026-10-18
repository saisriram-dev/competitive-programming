arr = [10, 20, 30, 40, 50]
n = len(arr)

target = 90
for mask in range(1 << n):
    subset = []

    for i in range(len(arr)):
        if mask & (1 << i):
            subset.append(arr[i])

    if sum(subset) == target:
        print("Found", subset)
