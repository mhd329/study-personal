import sys
sys.stdin = open("1236.txt", 'r')
N, M = map(int, sys.stdin.readline().split())

castle = []

for i in range(N):
    castle.append(sys.stdin.readline().rstrip())

row_check = [0] * M
column_check = [0] * N

for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row_check[j] = 1

for i in range(M):
    for j in range(N):
        if castle[j][i] == 'X':
            column_check[j] = 1

print(row_check.count(0) if row_check.count(0) > column_check.count(0) else column_check.count(0))