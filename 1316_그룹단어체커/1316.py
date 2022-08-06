import sys
sys.stdin = open("1316.txt", 'r')

N = int(sys.stdin.readline())
cnt = 0

for _ in range(N):
    stack = []
    ref = 1
    group_word = sys.stdin.readline().rstrip()
    
    for char in group_word:
        if char not in stack:
            stack.append(char)
        elif char in stack:
            if char == stack[-1]:
                pass
            else:
                ref = 0
                break
    if ref:
        cnt += 1

print(cnt)