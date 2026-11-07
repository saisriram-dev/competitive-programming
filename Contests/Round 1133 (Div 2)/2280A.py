import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if k % 2 != 0:
        even_a = sum(1 for x in a if x % 2 == 0)
        even_b = sum(1 for x in b if x % 2 == 0)
        return "YES" if even_b <= even_a else "NO"
    else:
        odd_a = sum(1 for x in a if x % 2 != 0)
        odd_b = sum(1 for x in b if x % 2 != 0)
        return "YES" if odd_b <= odd_a else "NO"

t = int(input())
for _ in range(t):
    print(solve())
