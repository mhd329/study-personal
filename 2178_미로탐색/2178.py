import sys
from collections import deque
sys.stdin = open("2178.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
maze = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not maze[nx][ny]:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] += maze[x][y]
                queue.append((nx, ny))
for _ in range(N):
    maze.append([*map(int, sys.stdin.readline().strip())])
bfs(0, 0)
print(maze[-1][-1])