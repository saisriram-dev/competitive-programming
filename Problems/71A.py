import sys
input = sys.stdin.readline

def solve():
    word = input().strip()   # read ONE word

    if len(word) > 10:
        result = word[0] + str(len(word) - 2) + word[-1]  # abbreviate the word
    else:
        result = word            # change this so result is the right thing to print
    print(result)

n = int(input())             # first line: how many words follow
for _ in range(n):
    solve()
