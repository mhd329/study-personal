import sys
sys.stdin = open("11441.txt", 'r')
N = int(sys.stdin.readline())
A = [0]
A += [*map(int, sys.stdin.readline().split())]
M = int(sys.stdin.readline())
t = [0] * (N + 1)
t[1] = A[1]
for idx in range(2, N + 1):
    t[idx] += t[idx - 1] + A[idx]
for _ in range(M):
    i, j = [*map(int, sys.stdin.readline().split())]
    print(t[j] - t[i - 1])