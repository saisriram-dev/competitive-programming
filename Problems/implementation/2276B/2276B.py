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
    words = set()
    count = 0

    if compress(num) not in words:
        words.add(compress(num))
        count += 1

    for i in range(1, len(num) - 1):
        if num[i - 1] == num[i + 1]:
            val = "0" if num[i] == "1" else "1"
            compressed = compress(num[:i] + val + num[i+1:])
            
            if compressed not in words:
                words.add(compressed)
                count += 1

    return count

t = int(input())
for _ in range(t):
    print(solve())
