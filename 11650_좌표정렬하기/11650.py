import sys
sys.stdin = open("11650.txt", 'r')
N = int(sys.stdin.readline())

for _ in range(N):
    x, y = map(int, sys.stdin.readline())
    minx = x
    miny = y
    