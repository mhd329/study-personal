import sys
sys.stdin = open("14501.txt", 'r')
N = int(sys.stdin.readline())
dp = [0] * (N + 1)
tp = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
for i in range(N):
    for j in range(tp[i][0] + i, N + 1):
        # print(f"i : {i}, j : {j}, dp[j] : {dp[j]}, dp[i] : {dp[i]}, tp[i][0] : {tp[i][0]}, tp[i][1] : {tp[i][1]}")
        if dp[j] < dp[i] + tp[i][1]:
            dp[j] = dp[i] + tp[i][1]
            # print(f"### {dp} ###")
print(dp[-1])