N = int(input())

dp = [0, 1, 3] + [0 for _ in range(N - 3)]

for i in range(3, N + 1):
    if i % 2: # 홀수
        dp[i] = dp[i - 1] * 3
    else: # 짝수
        dp[i] = dp[i - 1] * 4

print(dp)