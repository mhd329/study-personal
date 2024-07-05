import sys
sys.stdin = open("2738.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
res = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(2):
    for i in range(N):
        res[N - 1 - (N - 1 - i)] = [x + y for x, y in zip(res[N - 1 - (N - 1 - i)], [*map(int, sys.stdin.readline().split())])]
for i in res:
    print(*i)