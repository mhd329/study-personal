import sys
sys.stdin = open("2293.txt", 'r')
n, k = map(int, sys.stdin.readline().split())
dp = [0] * (k + 1)
dp[0] = 1
for _ in range(n):
    v = int(sys.stdin.readline())
    for t in range(1, k + 1):
        if t >= v:
            dp[t] += dp[t - v]
print(dp[-1])