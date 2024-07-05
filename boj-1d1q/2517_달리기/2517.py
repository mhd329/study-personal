# 시간 초과
'''
import sys
sys.setrecursionlimit(10**7)
from collections import deque
sys.stdin = open("2517.txt", 'r')
N = int(sys.stdin.readline())
track = deque()
arr = []
d = {}
def best(order, track, player):
    if not track or player > track[0][0]:
        track.appendleft((player, order))
        d[player] = order
        return track
    else:
        temp = track.popleft()
        order += 1
        best(order, track, player)
        track.appendleft(temp)
        return track
for _ in range(N):
    p = int(sys.stdin.readline())
    arr.append(p)
    o = 1
    while track:
        best(o, track, p)
        break
    else:
        track.append((p, o))
        d[p] = o
for i in arr:
    print(d[i])
'''
