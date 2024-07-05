import sys
sys.stdin = open("11659.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
arr = [0]
arr += [*map(int, sys.stdin.readline().split())]
total = [0] * (N + 1)
total[1] = arr[1]
for n in range(1, N + 1):
    total[n] = arr[n] + total[n - 1]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(total[j] - total[i - 1])