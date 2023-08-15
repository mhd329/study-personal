import sys
sys.stdin = open("9063.txt", 'r')

point_x = []
point_y = []

N = int(sys.stdin.readline())

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    point_x.append(x)
    point_y.append(y)

print((max(point_x) - min(point_x)) * (max(point_y) - min(point_y)))