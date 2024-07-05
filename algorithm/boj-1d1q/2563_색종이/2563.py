import sys
sys.stdin = open("2563.txt", 'r')

b = [[0 for i in range(100)] for j in range(100)]

T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    for i in range(n, n + 10):
        for j in range(m, m + 10):
            b[i][j] = 1
res = 0
for i in b:
    for j in i:
        if j == 1:
            res += 1

print(res)