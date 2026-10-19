import sys
input = sys.stdin.readline

def solve():
    x, y, k = map(int, input().split())
    
    C = y - x
    
    if x > C:
        return k * C
        
    total = 0
    i = 0
    
    while i < k:
        curr_x = x + i
        
        if curr_x > C:
            total += (k - i) * C
            break
            
        q = C // curr_x
        r = C % curr_x
        

        max_x_for_same_q = C // q
        steps_possible = max_x_for_same_q - curr_x + 1

        steps = min(k - i, steps_possible)
        
        sum_remainders = steps * r - q * (steps * (steps - 1) // 2)
        
        total += sum_remainders
        i += steps

    return total

t = int(input())
for _ in range(t):
    print(solve())
