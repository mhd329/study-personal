import sys
sys.stdin = open("2606.txt", 'r')
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
def dfs(start):
    stack = [start]
    visited = [False] * (N + 1)
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            stack.extend(graph[v])
    return visited
print(dfs(1).count(True) - 1)