import sys
from collections import deque
sys.stdin = open("2178.txt", 'r')

N, M = map(int, sys.stdin.readline().split())

queue = deque()
maze = []

for _ in range(N):
    maze.append([*map(int, list(sys.stdin.readline().strip()))])

def bfs(start):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < N and -1 < ny < M:
                if maze[nx][ny] == 1:
                    queue.append((nx, ny))
                    maze[nx][ny] += maze[x][y]

bfs((0, 0))
print(maze[-1][-1])