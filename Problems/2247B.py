import sys
input = sys.stdin.readline

def solve():
    n, k, m = map(int, input().split())
    
    # If k > m, no such array can exist by the pigeonhole principle
    if k > m:
        return "NO"
    
    # Construct the array
    a = [1] * n
    # The k-th element completes the sum to m
    a[k - 1] = m - (k - 1)
    
    # Format the output into a single string with a newline
    return "YES\n" + " ".join(map(str, a))

t = int(input())
for _ in range(t):
    print(solve())
