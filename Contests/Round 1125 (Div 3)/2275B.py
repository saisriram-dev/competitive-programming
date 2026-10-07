import sys
input = sys.stdin.readline

def solve():
    documents = int(input())
    comm_seq = input().strip()

    memory = []
    unprinted = []
    for i in range(1, documents + 1):
        if comm_seq[i - 1] == "1":
            memory.append(i)
        elif comm_seq[i - 1] == "2":
            if memory:
                memory.pop()
                unprinted.append(i)
        else:
            continue

    unprinted.extend(memory)
    unprinted.sort()

    print(len(unprinted))
    if len(unprinted) != 0:
        print(*unprinted)
    else:
        print()

t = int(input())
for _ in range(t):
    solve()
