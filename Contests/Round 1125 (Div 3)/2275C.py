import sys
from collections import Counter

input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    even = arr[::2]
    odd = arr[1::2]
    even_triads = []
    odd_triads = []

    for i in range(len(even) - 2):
        if len(even) < 3:
            break

        total = 0
        count = 0
        for j in range(i, i + 3):
            count += 1
            if count == 3:
                total -= even[j] 
            else:
                total += even[j]
        even_triads.append(total)

    for i in range(len(odd) - 2):
        if len(odd) < 3:
            break

        total = 0
        count = 0
        for j in range(i, i + 3):
            count += 1
            if count == 3:
                total -= odd[j]
            else:
                total += odd[j]
        odd_triads.append(total)

    ans = 0
    even_counter = Counter(even_triads)
    odd_counter = Counter(odd_triads)

    for val, count in even_counter.items():
        ans += count * odd_counter[val]

    cnt = Counter()
    for i in range(len(even_triads)):
        if i >= 3:
            cnt[even_triads[i - 3]] += 1
        ans += cnt[even_triads[i]]

    cnt = Counter()
    for i in range(len(odd_triads)):
        if i >= 3:
            cnt[odd_triads[i - 3]] += 1
        ans += cnt[odd_triads[i]]

    return ans


t = int(input())
for _ in range(t):
    print(solve())
