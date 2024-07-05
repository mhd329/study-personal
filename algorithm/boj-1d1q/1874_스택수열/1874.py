import sys
sys.stdin = open("1874.txt", 'r')
N = int(sys.stdin.readline())
res = []
ans = []
stack1 = []
stack2 = []
idx = 1
res = [int(sys.stdin.readline()) for _ in range(N)]
for i in res:
    for j in range(idx, i + 1):
        stack1.append(j)
        ans.append("+")
        idx += 1
    try:
        while not stack2 or stack2[-1] != i:
            stack2.append(stack1.pop())
            ans.append("-")
    except:
        print("NO")
        break
else:
    for k in ans:
        print(k)
# 더 짧은 풀이
'''
n = int(input())
seq = [int(input()) for _ in range(n)]

stack = []
result = []

for i in range(1, n+1):
    stack.append(i)
    result.append("+")
    while stack and stack[-1] == seq[0]:
        stack.pop()
        result.append("-")
        seq.pop(0)

if seq:
    print("NO")
else:
    for op in result:
        print(op)
'''