import sys
from collections import deque
sys.stdin = open("24444.txt", 'r')

queue = deque()
order = []
N, M, R = map(int, sys.stdin.readline().split())
visited = [False] * (N + 1)
visited[0] = True

E = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    E[x].append(y)
    E[y].append(x)

for V in E:
    V.sort()
[*map(queue.append, E[R])]
order.append(R)
visited[R] = True
while queue:
    v = queue.popleft()
    if v not in order:
        order.append(v)
        visited[v] = True
        [*map(queue.append, E[v])]
if False in visited:
    order.append(0)
print(order)