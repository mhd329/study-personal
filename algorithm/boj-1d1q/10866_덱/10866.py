import sys
from collections import deque
sys.stdin = open("10866.txt", 'r')
N = int(sys.stdin.readline())
dq = deque()
for _ in range(N):
    c = sys.stdin.readline().split()
    if c[0] == "push_front":
        dq.appendleft(int(c[1]))
    elif c[0] == "push_back":
        dq.append(int(c[1]))
    elif c[0] == "pop_front":
        print(dq.popleft() if dq else -1)
    elif c[0] == "pop_back":
        print(dq.pop() if dq else -1)
    elif c[0] == "size":
        print(len(dq))
    elif c[0] == "empty":
        print(0 if dq else 1)
    elif c[0] == "front":
        print(dq[0] if dq else -1)
    else:
        print(dq[-1] if dq else -1)