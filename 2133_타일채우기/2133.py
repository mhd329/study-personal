N = int(input())

dp = [1, 0, 3] + [0 for _ in range(N - 2)]

for i in range(3, N + 1):
    if not i % 2: # 홀수
        dp[i] = dp[i - 2] ** 2

print(dp)