# N = int(input())
# dp = [0] * (N + 1)
# dp[1] = -1
# dp[2] = -1
# for i in range(3, N + 1):
#     if i < 5:
#         dp[i] = dp[i - 3] + 1 if dp[i - 3] != -1 else -1
#     else:
#         a = dp[i - 3] + 1 if dp[i - 3] != -1 else -1
#         b = dp[i - 5] + 1 if dp[i - 5] != -1 else -1
#         dp[i] = min(a, b) if a != -1 and b != -1 else max(a, b)
# print(dp[N])

N = int(input())
dp = [0] * (N + 1)
dp[0] = 1
for i in range(3, N + 1):
    if i < 5:
        dp[i] = dp[i - 3]
    elif i == 5:
        dp[i] = 1
    else:
        a = dp[i - 3] + 1 if dp[i - 3] else 0
        b = dp[i - 5] + 1 if dp[i - 5] else 0
        dp[i] = min(a, b) if a and b != 0 else max(a, b)
print(dp[N] if dp[N] else -1)