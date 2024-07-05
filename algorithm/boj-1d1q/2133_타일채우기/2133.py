N = int(input())
dp = [1, 0, 3] + [0 for _ in range(N - 2)]
for i in range(4, N + 1):
    if not i % 2:
        dp[i] = dp[i - 2] * dp[2]
        for j in range(i - 4, -1, -2):
            dp[i] = dp[i] + (dp[j] * 2)
print(dp[N])