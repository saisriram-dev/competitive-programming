import sys
input = sys.stdin.readline

def ask(l, r):
    print(f"? {l} {r}")
    sys.stdout.flush()
    res = int(input())
    if res == -1:
        sys.exit(0)
    return res

def solve():
    n = int(input())
    y = ask(1, n)              

    if 0 < y < n:              
        z = ask(1, y)          
        if z < y:
            print("! YES")
        else:
            print("! NO")
    else:
        print("! NO")      
    sys.stdout.flush()

t = int(input())
for _ in range(t):
    solve()
