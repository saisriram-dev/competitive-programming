t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    # Case 1: starts with 1
    if s[0] == '1':
        print(s.count('0'))
        continue

    # Case 2: starts with 0
    total_zeros = s.count('0')

    ones_before = 0
    zeros_after = total_zeros

    ans = zeros_after

    for ch in s:

        if ch == '1':
            ones_before += 1
        else:
            zeros_after -= 1

        cost = ones_before + zeros_after

        ans = min(ans, cost)

    print(ans)
