import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + nums[i - 1]

    balanced = 0
    remainder_count = defaultdict(int)

    for j in range(n + 1):
        valid_i = j - k - 1
        if valid_i >= 0:
            remainder_count[pref[valid_i] % k] += 1

        current_rem = pref[j] % k
        balanced += remainder_count[current_rem]

    return balanced
    

t = int(input())
for _ in range(t):
    print(solve())
