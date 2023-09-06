from collections import deque

N, K = map(int, input().split())
q = deque([i for i in range(1, N + 1)])
res = []
while q:
    q.rotate(-(K - 1))
    e = q.popleft()
    res.append(e)
print(str(res).replace("[", "<").replace("]", ">"))
