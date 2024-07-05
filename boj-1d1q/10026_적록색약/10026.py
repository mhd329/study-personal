import sys
from collections import deque
sys.stdin = open("10026.txt", 'r')

N = int(sys.stdin.readline())
field = []

for _ in range(N):
    field.append(list(sys.stdin.readline().strip()))

def bfs_r(start):
    queue_r = deque()
    queue_r.append(start)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue_r:
        x, y = queue_r.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < N and -1 < ny < N:
                if field[nx][ny] == "R":
                    field[nx][ny] = 1
                    queue_r.append((nx, ny))

def bfs_g(start):
    queue_g = deque()
    queue_g.append(start)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue_g:
        x, y = queue_g.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < N and -1 < ny < N:
                if field[nx][ny] == "G":
                    field[nx][ny] = 1
                    queue_g.append((nx, ny))

def bfs_rg(start):
    queue_rg = deque()
    queue_rg.append(start)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue_rg:
        x, y = queue_rg.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < N and -1 < ny < N:
                if field[nx][ny] == 1:
                    field[nx][ny] = 0
                    queue_rg.append((nx, ny))

def bfs_b(start):
    queue_b = deque()
    queue_b.append(start)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue_b:
        x, y = queue_b.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < N and -1 < ny < N:
                if field[nx][ny] == "B":
                    field[nx][ny] = 0
                    queue_b.append((nx, ny))

cnt_r = 0
cnt_g = 0
cnt_rg = 0
cnt_b = 0

for i in range(N):
    for j in range(N):
        if field[i][j] == "R":
            field[i][j] = 1
            bfs_r((i, j))
            cnt_r += 1
        elif field[i][j] == "G":
            field[i][j] = 1
            bfs_g((i, j))
            cnt_g += 1
        elif field[i][j] == "B":
            field[i][j] = 0
            bfs_b((i, j))
            cnt_b += 1

for i in range(N):
    for j in range(N):
        if field[i][j]:
            field[i][j] = 0
            bfs_rg((i, j))
            cnt_rg += 1

print(cnt_r + cnt_g + cnt_b, cnt_rg + cnt_b)