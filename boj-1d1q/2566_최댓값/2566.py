import sys
sys.stdin = open("2566.txt", 'r')

n = []
m = 0
a, b = 0, 0

for _ in range(9):
    n.append([*map(int, sys.stdin.readline().split())])

for i in range(9):
    for j in range(9):
        if n[i][j] >= m:
            m = n[i][j]
            a, b = i, j

print(m)
print(a + 1, b + 1)