recipe = str(input().strip())
b, s, c = recipe.count("B"), recipe.count("S"), recipe.count("C")
nb, ns, nc = list(map(int, input().split()))  # Fixed: added .split()
pb, ps, pc = list(map(int, input().split()))  # Fixed: added .split()
money = int(input())

def check(x):
    b_need = s_need = c_need = 0
    pb_need = max(0, (x * b) - nb) * pb
    ps_need = max(0, (x * s) - ns) * ps
    pc_need = max(0, (x * c) - nc) * pc

    total = pb_need + ps_need + pc_need
    return True if money >= total else False

low, high = 0, 10 ** 13
ans = 0

while low <= high:
    mid = low + (high - low) // 2

    if check(mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)
