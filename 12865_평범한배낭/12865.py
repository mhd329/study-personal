import sys
sys.stdin = open("12865.txt", 'r')
N, K = map(int, sys.stdin.readline().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    w, v = map(int, sys.stdin.readline().split())
    for j in range(1, K + 1):
        if j >= w:
            dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[N][K])