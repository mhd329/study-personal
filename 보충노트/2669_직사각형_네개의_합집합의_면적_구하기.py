import sys
sys.stdin = open("2669_직사각형_네개의_합집합의_면적_구하기.txt", 'r')

m = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            m[i][j] = 1

print(sum(map(sum, m)))