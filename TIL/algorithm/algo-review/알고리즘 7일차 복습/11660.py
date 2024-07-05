import sys
sys.stdin = open("11660.txt", 'r')

N, M = map(int, sys.stdin.readline().split())

arr = []
dp = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N):
    arr.append([*map(int, sys.stdin.readline().split())])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = arr[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for _ in range(M):
    i, j, x, y = map(int, sys.stdin.readline().split())
    ans = dp[x][y] - dp[i - 1][y] - dp[x][j - 1] + dp[i - 1][j - 1]
    print(ans)