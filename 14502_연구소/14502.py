import sys
from collections import deque
sys.stdin = open("14502.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
building = []
for _ in range(N):
    building.append([*map(int, sys.stdin.readline().split())])
visited = [[0] * M for _ in range(N)]
def bfs(m, n):
    queue = deque()
    queue.append(m, n)
for i in range(N):
    for j in range(M):
        if building[i][j] == 0:
            building[i][j] = 1
            visited[i][j] = 1
            continue