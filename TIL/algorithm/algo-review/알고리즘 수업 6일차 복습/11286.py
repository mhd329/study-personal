import sys
from heapq import heappush, heappop

sys.stdin = open("11286.txt", "r")

N = int(sys.stdin.readline())
h = []

for _ in range(N):
    ele = int(sys.stdin.readline())
    if ele:
        heappush(h, (abs(ele), ele))
    else:
        if len(h):
            print(heappop(h)[1])
        else:
            print(0)
