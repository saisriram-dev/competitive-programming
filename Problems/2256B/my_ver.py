import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    # Convert string directly into a list of characters
    arr = list(input().strip())

    complements = {"0": "1", "1": "0", "?": "?"}

    odd, even = [], []
    for i in range(len(arr)):
        if i % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])

    # 1. Count '?' BEFORE modifying the lists to keep your exact ways logic
    odd_count = odd.count("?")
    even_count = even.count("?")

    # 2. FIX: Propagate known values so your adjacent check catches long-range contradictions
    # Forward pass for odd
    for k in range(1, len(odd)):
        if odd[k-1] != "?" and odd[k] == "?":
            odd[k] = complements[odd[k-1]]
    # Backward pass for odd
    for k in range(len(odd)-2, -1, -1):
        if odd[k+1] != "?" and odd[k] == "?":
            odd[k] = complements[odd[k+1]]

    # Forward pass for even
    for k in range(1, len(even)):
        if even[k-1] != "?" and even[k] == "?":
            even[k] = complements[even[k-1]]
    # Backward pass for even
    for k in range(len(even)-2, -1, -1):
        if even[k+1] != "?" and even[k] == "?":
            even[k] = complements[even[k+1]]

    # 3. YOUR EXACT LOGIC: Verifying if adjacent pairs are not equal in both lists
    i = 0
    j = 1
    while j < len(odd):
        if odd[j] == odd[i] == "?":
            i += 1
            j += 1
        elif odd[j] != odd[i]:
            i += 1
            j += 1
        else:
            return 0

    i = 0
    j = 1
    while j < len(even):
        if even[j] == even[i] == "?":
            i += 1
            j += 1
        elif even[j] != even[i]:
            i += 1
            j += 1
        else:
            return 0

    # YOUR EXACT LOGIC: Calculating ways
    if even_count == len(even):
        ways_even = 2
    else:
        ways_even = 1

    if odd_count == len(odd):
        ways_odd = 2
    else:
        ways_odd = 1

    # Added modulo 998244353 as requested by the problem description[cite: 2]
    return (ways_odd * ways_even) % 998244353


t = int(input())
for _ in range(t):
    print(solve())
