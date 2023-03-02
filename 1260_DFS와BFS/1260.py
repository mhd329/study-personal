import sys
from collections import deque
sys.stdin = open("1260.txt", 'r')

N, M, V = [*map(int, sys.stdin.readline().split())]

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
'''
visited1 = [False]
visited2 = [False]
q1 = deque([])
q2 = deque([])
for x in graph:
    x.sort()

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
'''

visited_dfs = []
visited_bfs = []

for edge in graph:
    edge.sort()

queue = deque([])

def dfs(v):
    if v not in visited_dfs:
        visited_dfs.append(v)
        for i in graph[v]:
            dfs(i)

def bfs(v):
    visited_bfs.append(v)
    queue.append(v)
    while queue:
        i = queue.popleft()
        for j in graph[i]:
            if j not in visited_bfs:
                visited_bfs.append(j)
                queue.append(j)

dfs(V)
bfs(V)

print(*visited_dfs)
print(*visited_bfs)