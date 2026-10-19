import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
money = 0
total = sum(arr)
coins = 0

j = len(arr) - 1
while money <= total:
    money += arr[j]
    total -= arr[j]
    coins += 1
    j -= 1

print(coins)
