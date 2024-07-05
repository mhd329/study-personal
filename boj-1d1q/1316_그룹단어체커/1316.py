import sys
sys.stdin = open("1316.txt", 'r')

N = int(sys.stdin.readline())
no = 0

for _ in range(N):
    stack = []
    group_word = sys.stdin.readline().rstrip()
    
    for char in group_word:
        if char not in stack:
            stack.append(char)
        elif char in stack:
            if char != stack[-1]:
                no += 1 # 그룹 단어가 아님
                break

print(N - no)