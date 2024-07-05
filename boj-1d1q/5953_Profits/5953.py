import sys
sys.stdin = open("5953.txt", 'r')
N = int(sys.stdin.readline())
dp = [0] * N
dp[0] = int(sys.stdin.readline())
for i in range(1, N):
    n = int(sys.stdin.readline())
    dp[i] = max(dp[i - 1] + n, n)
print(max(dp))