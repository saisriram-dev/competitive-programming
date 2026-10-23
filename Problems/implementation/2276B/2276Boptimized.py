import sys
input = sys.stdin.readline

def compress(string):
    res = []
    for char in string:
        if not res or res[-1] != char:
            res.append(char)
    return "".join(res)

def solve():
    num = input().strip()
    n = len(num)

    compressed = []
    for char in num:
        if not compressed or compressed[-1] != char:
            compressed.append(char)
    base_len = len(compressed)

    possible_lengths = {base_len}

    for i in range(n - 2):
        if num[i] == num[i + 1] == num[i + 2]:
            possible_lengths.add(base_len + 2)
            break

    for i in range(n - 2):
        if num[i] == num[i + 2] and num[i + 1] != num[i]:
            possible_lengths.add(base_len - 2)
            break

    return len(possible_lengths)

t = int(input())
for _ in range(t):
    print(solve())
