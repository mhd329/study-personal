from collections import deque
def bfs(v, maps):
    x, y = v
    total = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append((x, y))
    total += maps[x][y]
    maps[x][y] = "X"
    r = len(maps)
    c = len(maps[0])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < r and -1 < ny < c:
                if maps[nx][ny] != "X":
                    queue.append((nx, ny))
                    total += maps[nx][ny]
                    maps[nx][ny] = "X"
    return total
    
def solution(maps):
    answer = []
    maps = [*map(list, maps)]
    r = len(maps)
    c = len(maps[0])
    for i in range(r):
        for j in range(c):
            if maps[i][j] != "X":
                maps[i][j] = int(maps[i][j])
    for i in range(r):
        for j in range(c):
            if maps[i][j] != "X":
                answer.append(bfs((i, j), maps))
    answer.sort()
    if answer:
        return answer
    else:
        return [-1]