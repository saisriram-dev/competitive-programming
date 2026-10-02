import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    seq = input().strip()

    initial_len = 0
    for i in range(1, n):
        if seq[i] != seq[i - 1]:
            initial_len += 1

    max_reduction = 0
    for i in range(1, n - 1):
        if seq[i] != seq[i - 1] and seq[i - 1] == seq[i + 1]:
            max_reduction = 2
            break
        elif seq[i] != seq[i - 1] and seq[i] != seq[i + 1]:
            max_reduction = 1

    return initial_len - max_reduction

t = int(input().strip())
for _ in range(t):
    print(solve())
