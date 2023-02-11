import sys
from collections import deque
sys.stdin = open("1966.txt", 'r')
T = int(sys.stdin.readline())
for _ in range(T):
    N, idx = map(int, sys.stdin.readline().split())
    docs = deque([*map(int, sys.stdin.readline().split())])
    cnt = 0
    while docs:
        mx = max(docs)
        n = docs.popleft()
        idx -= 1
        if mx == n:
            cnt += 1
            if idx < 0:
                print(cnt)
                break
        else:
            docs.append(n)
            if idx < 0 :
                idx = len(docs) - 1