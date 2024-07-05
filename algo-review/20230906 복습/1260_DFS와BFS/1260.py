import sys
from collections import deque

sys.stdin = open("1260.txt", "r")

N, M, V = map(int, sys.stdin.readline().split())

edges = [[] for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    edges[x].append(y)
    edges[y].append(x)

dfs_visited = []
bfs_visited = []
q = deque()


def dfs(V):
    if V not in dfs_visited:
        dfs_visited.append(V)
        for v in edges[V]:
            dfs(v)


def bfs(V):
    bfs_visited.append(V)
    q.append(V)
    while q:
        v = q.popleft()
        for i in edges[v]:
            if i not in bfs_visited:
                bfs_visited.append(i)
                q.append(i)


dfs(V)
bfs(V)
print(*dfs_visited)
print(*bfs_visited)
