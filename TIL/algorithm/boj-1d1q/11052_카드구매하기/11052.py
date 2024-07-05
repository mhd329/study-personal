import sys
sys.stdin = open("11052.txt", 'r')
N = int(sys.stdin.readline())
P = [0] + [*map(int, sys.stdin.readline().split())]
dp = [0] * (N + 1)
dp[1] = P[1]
for i in range(2, N + 1):
    for j in range(i, 0, -1):
        dp[i] = max(dp[i], P[j] + dp[i - j])
print(dp[-1])