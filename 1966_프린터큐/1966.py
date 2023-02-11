import sys
from collections import deque
sys.stdin = open("1966.txt", 'r')
T = int(sys.stdin.readline())
for _ in range(T):
    cnt = 0
    N, idx = map(int, sys.stdin.readline().split())
    docs = deque([*map(int, sys.stdin.readline().split())])
    while docs:
        while docs[0] < max(docs):
            docs.rotate(-1)
            idx -= 1
            if idx < 0:
                idx = len(docs)
        docs.popleft()
        cnt += 1