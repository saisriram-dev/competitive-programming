from bisect import bisect_left

arr = list(map(int, input().split()))
tails = []

for v in arr:
    i = bisect_left(tails, v)

    if i == len(tails):
        tails.append(v)
    else:
        tails[i] = v

print(len(tails))
