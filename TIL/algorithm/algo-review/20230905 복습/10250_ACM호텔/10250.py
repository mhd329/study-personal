import sys
import math

sys.stdin = open("10250.txt", "r")
T = int(sys.stdin.readline())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    l = 0
    while l + len(str(math.ceil(N / H))) < 2:
        l += 1
    w = N // H
    h = N - (H * w) if N % H else H
    print(h, end="")
    for _ in range(l):
        print("0", end="")
    print(math.ceil(N / H))
