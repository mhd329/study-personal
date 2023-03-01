import sys
from collections import deque
sys.stdin = open("1260.txt", 'r')

N, M, V = [*map(int, sys.stdin.readline().split())]

graph = [[] for _ in range(N + 1)]
for _ in range(1, M + 1):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)
q1 = deque([])
q2 = deque([])
for x in graph[1:]:
    x.sort()
print(graph)
# bfs

def bfs(start, visited, q):
    if not visited[start]:
        visited[start] = True
        q.append(start)
        while q:
            v = q.popleft()
            bfs(v, visited, q)
            print(v)
            for i in graph[v]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)

# dfs

def dfs(start, visited, q):
    if not visited[start]:
        visited[start] = True
        print(start)
        q.append(start)
        while q:
            v = q.popleft()
            for i in graph[v]:
                dfs(i, visited, q)
dfs(V, visited1, q1)
bfs(V, visited2, q2)