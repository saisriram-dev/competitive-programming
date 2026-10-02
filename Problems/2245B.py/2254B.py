import sys

def solve():
    n = int(input().strip())
    seq = input().strip()

    blocks = []
    i = 0
    while i < n:
        j = i
        while j < n and seq[j] == seq[i]:
            j += 1
        blocks.append((seq[i], j - i))
        i = j

    m = len(blocks)
    seen = set()

    
    for i in range(1, m - 1):
        char, width = blocks[i]
        
        if width == 1:
            if blocks[i - 1][0] == blocks[i + 1][0]:
                seen.add("YES")  
            else:
                seen.add("NO")   

    if "YES" in seen:
        return m - 2
    elif "NO" in seen:
        return m - 1
    else:
        return m


t = int(input().strip())
for _ in range(t):
    print(solve())
