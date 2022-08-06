import sys
from pprint import pprint
sys.stdin = open("1236_성지키기.txt", 'r')

N, M = map(int, sys.stdin.readline().split())

castle = []
r_cnt = 0
ck = []

for _ in range(N):
    castle.append(sys.stdin.readline().rstrip())

for r in castle:
    if 'X' not in r:
        r_cnt += 1

for c in range(M):
    for r in range(N):
        if 'X' == castle[r][c]:
            ck.append(1)
            break

c_cnt = M - len(ck)

print(r_cnt if r_cnt >= c_cnt else c_cnt)