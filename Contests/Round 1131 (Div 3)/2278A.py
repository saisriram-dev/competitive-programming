
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    p = input().strip()
    q = input().strip()

    freq = [0] * 26

    for char in p:
        freq[ord(char) - ord('a')] += 1

    for char in q:
        freq[ord(char) - ord('a')] -= 1

    for i in range(26):
        if freq[i] < 0:
            return "NO"

    target = [0] * 26

    for char in "six":
        target[ord(char) - ord('a')] += 1

    if freq == target:
        return "YES"

    return "NO"


t = int(input())

for _ in range(t):
    print(solve())
