import collections
N = int(input())
q = collections.deque([i for i in range(1, N + 1)])
while len(q) != 1:
    card = q.popleft()
    q.append(q.popleft())
print(*q)