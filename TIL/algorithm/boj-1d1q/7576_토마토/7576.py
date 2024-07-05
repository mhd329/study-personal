import sys
from collections import deque
sys.stdin = open("7576.txt", 'r')
M, N = map(int, sys.stdin.readline().split())
def bfs(box, start):
    mx = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue += start
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if box[nx][ny] == 0:
                box[nx][ny] += box[x][y] + 1
                if box[nx][ny] > mx:
                    mx = box[nx][ny]
                queue.append((nx, ny))
    for j in box:
        if 0 in j:
            return -1
    return mx - 1
def box_search(n, m):
    box = []
    start = []
    execution = False
    for _ in range(n):
        box.append([*map(int, sys.stdin.readline().split())])
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                execution = True
            if box[i][j] == 1:
                start.append((i, j))
    if not execution:
        return 0
    else:
        return (box, start)
res = box_search(N, M)
print(bfs(*res) if res else res)