import sys
from heapq import heappop, heappush

sys.stdin = open("2750.txt", "r")

N = int(sys.stdin.readline())
h = []

for _ in range(N):
    n = int(sys.stdin.readline())
    heappush(h, n)

for _ in range(N):
    print(heappop(h))
