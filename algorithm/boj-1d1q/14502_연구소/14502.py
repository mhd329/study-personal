# python 시간초과, pypy 정답
'''
import sys
from copy import deepcopy
from collections import deque
sys.stdin = open("14502.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
labo = []
for _ in range(N):
    labo.append([*map(int, sys.stdin.readline().split())])
ans = 0
def bfs():
    global ans
    queue = deque()
    temp = deepcopy(labo)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < N and -1 < ny < M:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))
    res = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                res += 1
    ans = max(res, ans)
cnt = 0
def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if labo[i][j] == 0 :
                labo[i][j] = 1
                wall(cnt + 1)
                labo[i][j] = 0
wall(cnt)
print(ans)
'''

import sys
from copy import deepcopy
from collections import deque
sys.stdin = open("14502.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
labo = []
for _ in range(N):
    labo.append([*map(int, sys.stdin.readline().split())])
ans = 0
def bfs():
    global ans
    queue = deque()
    temp = deepcopy(labo)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                temp[i][j] = 3
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if -1 < nx < N and -1 < ny < M:
                            if temp[nx][ny] == 0 or temp[nx][ny] == 2:
                                temp[nx][ny] = 3
                                queue.append((nx, ny))
    res = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                res += 1
    ans = max(res, ans)
cnt = 0
def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if labo[i][j] == 0 :
                labo[i][j] = 1
                wall(cnt + 1)
                labo[i][j] = 0
wall(cnt)
print(ans)