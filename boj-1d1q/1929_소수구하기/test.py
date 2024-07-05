import sys
M, N = map(int, sys.stdin.readline().split())

p = [False, False] + ([True] * (N - 1))

for n in range(2, N + 1):
    if p[n] == True:
        for i in range(2 * n, N + 1, n):
            p[i] = False

for j in range(M, N + 1):
    if p[j] == True:
        print(j)