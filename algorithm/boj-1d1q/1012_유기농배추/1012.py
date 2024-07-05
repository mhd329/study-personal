import sys
sys.stdin = open("1012.txt", 'r')
'''
sys.setrecursionlimit(10 ** 6)
def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    elif field[x][y]:
        field[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x, y - 1)
        return True
    return False
T = int(sys.stdin.readline())
for _ in range(T):
    total = 0
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                total += 1
    print(total)
'''
from collections import deque
queue = deque()
def bfs(x, y):
    first_x = x
    first_y = y
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if field[nx][ny] == 1:
                field[nx][ny] += field[x][y]
                queue.append((nx, ny))
    return field[x][y]
T = int(sys.stdin.readline())
for _ in range(T):
    res = []
    total = 0
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    for x in range(N):
        for y in range(M):
            if field[x][y] == 1:
                res.append(bfs(x, y))
    print(len(res))