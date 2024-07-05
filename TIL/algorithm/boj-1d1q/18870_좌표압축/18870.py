import sys
sys.stdin = open("18870.txt", 'r')
N = int(sys.stdin.readline())
X = [*map(int, sys.stdin.readline().split())]
x = sorted(set(X))
d = {}
for i in range(len(x)):
    d[x[i]] = i
for j in range(len(X)):
    X[j] = d[X[j]]
print(*X)