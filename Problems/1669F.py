import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    i = 0
    j = n - 1

    left = arr[i]
    right = arr[j]
    
    candies = [0]

    while i < j:
        if left > right:
            j -= 1
            right += arr[j]

        elif right > left:
            i += 1
            left += arr[i]

        elif left == right:
            candies.append((i + 1) + (n - j))
            i += 1
            j -= 1

            if i < j:
                left += arr[i]
                right += arr[j]
    
    return max(candies)

t = int(input())
for _ in range(t):
    print(solve())
