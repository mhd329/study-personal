import sys
sys.stdin = open("17298.txt", 'r')
N = int(sys.stdin.readline())
A = [*map(int, sys.stdin.readline().split())]
ans = [-1] * N
stack = []
for i in range(N):
    while stack and A[i] > A[stack[-1]]:
        ans[stack.pop()] = A[i]
    stack.append(i)
print(*ans)