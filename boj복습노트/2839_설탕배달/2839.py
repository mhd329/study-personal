N = int(input())
dp = [0] * (N + 1)
dp[1] = -1
dp[2] = -1
for i in range(3, N + 1):
    if i < 5:
        dp[i] = dp[i - 3] + 1 if dp[i - 3] != -1 else -1
    else:
        a = dp[i - 3] + 1 if dp[i - 3] != -1 else -1
        b = dp[i - 5] + 1 if dp[i - 5] != -1 else -1
        dp[i] = min(a, b) if a != -1 and b != -1 else max(a, b)
print(dp[N])