import sys
sys.stdin = open("10810.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
arr = [0] + [0 for _ in range(N)]
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for idx in range(i, j + 1):
        arr[idx] = k
print(*arr[1:])