import sys
sys.stdin = open("2738.txt", 'r')

n, m = map(int, sys.stdin.readline().split())
a = []
b = []

for _ in range(n):
    a.append([*map(int, sys.stdin.readline().split())])

for _ in range(n):
    b.append([*map(int, sys.stdin.readline().split())])

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=' ')
    print()