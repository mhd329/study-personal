import sys
sys.stdin = open("2667.txt", 'r')
'''
apart = []
N = int(sys.stdin.readline())
for _ in range(N):
    apart.append([*map(int, sys.stdin.readline().strip())])
total = 0
cnt = 0
res = []
def dfs(x, y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if apart[x][y] == 0:
        return False
    if apart[x][y] == 1:
        cnt += 1
        apart[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x, y - 1)
        return True
for i in range(N):
    for j in range(N):
        if dfs(i, j):
            total += 1
            res.append(cnt)
            cnt = 0
res.sort()
print(total)
for _ in res:
    print(_)
'''
apart = []
N = int(sys.stdin.readline())
for _ in range(N):
    apart.append([*map(int, sys.stdin.readline().strip())])
total = 0
res = []
def dfs(x, y, cnt):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False, cnt
    if apart[x][y] == 0:
        return False, cnt
    if apart[x][y] == 1:
        cnt += 1
        apart[x][y] = 0
        cnt = dfs(x - 1, y, cnt)[1]
        cnt = dfs(x, y + 1, cnt)[1]
        cnt = dfs(x + 1, y, cnt)[1]
        cnt = dfs(x, y - 1, cnt)[1]
        return True, cnt
for i in range(N):
    for j in range(N):
        a, b = dfs(i, j, 0)
        if a:
            total += 1
            res.append(b)
            cnt = 0
res.sort()
print(total)
for _ in res:
    print(_)