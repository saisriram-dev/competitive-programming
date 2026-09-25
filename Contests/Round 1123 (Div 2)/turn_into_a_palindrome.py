import sys
input = sys.stdin.readline

def solve():
    line1 = input().split()
    if not line1:
        return
    n = int(line1[0])
    c = line1[1]

    word = input().strip()
    coins = 0

    for i in range(n // 2):
        left = word[i]
        right = word[n - 1 - i]

        if left == right:
            continue

        if left != c and right != c:
            coins += 2
        else:
            coins += 1

    print(coins)

if __name__ == "__main__":
    t_str = input().strip()
    if t_str:
        t = int(t_str)
        for _ in range(t):
            solve()
