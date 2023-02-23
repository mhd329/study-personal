import sys
sys.stdin = open("11052.txt", 'r')
N = int(sys.stdin.readline())
P = [0] + [*map(int, sys.stdin.readline().split())]
dp = [0] * (N + 1)
dp[1] = P[1]
for i in range(2, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + P[j])
print(dp[-1])