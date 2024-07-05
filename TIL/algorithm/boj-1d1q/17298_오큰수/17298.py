import sys
sys.stdin = open("17298.txt", 'r')
N = int(sys.stdin.readline())
A = [*map(int, sys.stdin.readline().split())]
NGE = [-1] * N
stack = [0]
for i in range(1, N):
    while stack and A[i] > A[stack[-1]]:
        NGE[stack.pop()] = A[i]
    stack.append(i)
print(*NGE)