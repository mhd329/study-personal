T = int(input())

dp = [0] * 41
dp[1] = 1

for _ in range(T):
    N = int(input())
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    if N:
        print(dp[N - 1], dp[N])
    else:
        print(1, dp[N])