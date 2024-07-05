import sys
sys.stdin = open("10813.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
arr = [0] + [i for i in range(1, N + 1)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    a = arr[i]
    b = arr[j]
    arr[i] = b
    arr[j] = a
print(*arr[1:])