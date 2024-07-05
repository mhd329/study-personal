import sys
from collections import deque
sys.stdin = open("2667.txt", 'r')

N = int(sys.stdin.readline())
apt = []
apts = []
for _ in range(N):
    apt.append([*map(int, list(sys.stdin.readline().strip()))])

def bfs(start):
    cnt = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    x, y = start
    apt[x][y] = 0
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < N and -1 < ny < N:
                if apt[nx][ny] == 1:
                    apt[nx][ny] = 0
                    cnt += 1
                    queue.append((nx, ny))
    return cnt

total = 0

for i in range(N):
    for j in range(N):
        if apt[i][j]:
            apts.append(bfs((i, j)))
            total += 1

apts.sort()
print(total)
for i in apts:
    print(i)