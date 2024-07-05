import sys
sys.stdin = open("9251.txt", 'r')
S1 = sys.stdin.readline().strip()
S2 = sys.stdin.readline().strip()
N = len(S1)
M = len(S2)
dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if S1[i - 1] == S2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])