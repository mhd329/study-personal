import sys
sys.stdin = open("1712.txt", 'r')

A, B, C = map(int, sys.stdin.readline().split())

if B < C:
    print(A // (C - B) + 1)
else:
    print(-1)