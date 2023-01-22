import sys
sys.stdin = open("12865.txt", 'r')
N, K = map(int, sys.stdin.readline().split())
dp = [0] * (K + 1)
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    for i in range(w, K + 1):
        dp[i] = max(dp[i - w] + v, dp[i])
print(max(dp))