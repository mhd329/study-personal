import sys

sys.stdin = open("2167.txt", "r")

N, M = map(int, sys.stdin.readline().split())

dp = [[0] * (M + 1) for _ in range(N + 1)]
# dp2 = [[0] * (M + 1)] * (N + 1)
# 얕은복사가 되기 때문에 이상하게 저장된다.

arr = []

for _ in range(N):
    arr.append([*map(int, sys.stdin.readline().split())])

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = arr[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

K = int(sys.stdin.readline())
for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    ans = dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1]
    print(ans)