from collections import deque
N, K = map(int, input().split())
def bfs(n, k):
    visited = [0] * 100001
    queue = deque()
    queue.append(n)
    while queue:
        v = queue.popleft()
        if v == k:
            return visited[v]
        position = [v - 1, v + 1, v * 2]
        for i in position:
            if i >= 0 and i <= 100000 and not visited[i]:
                visited[i] += (visited[v] + 1)
                queue.append(i)
print(bfs(N, K))