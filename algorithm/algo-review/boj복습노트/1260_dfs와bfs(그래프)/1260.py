import sys
from collections import deque

sys.stdin = open("1260.txt", 'r')

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(start):
    for v in graph:
        v.sort(reverse=True)
    stack = [start]
    visited = []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            stack.extend(graph[v])
    return visited

def bfs(start):
    for v in graph:
        v.sort()
    queue = deque([start])
    visited = []
    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.append(v)
            queue.extend(graph[v])
    return visited

print(*dfs(V))
print(*bfs(V))