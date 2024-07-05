import sys
sys.stdin = open("11053.txt", 'r')
N = int(sys.stdin.readline())
dp = [1] * N
A = [*map(int, sys.stdin.readline().split())]
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))