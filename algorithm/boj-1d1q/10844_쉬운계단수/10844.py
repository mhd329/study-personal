N = int(input())
dp = [[0] * 10 for _ in range(0, N + 1)]
for a in range(1, 10):
    dp[1][a] = 1
for i in range(2, N + 1):
    # j == 0 일때를 추가하는 이유는 101 같이 뒤가 0 으로 시작하는 경우를 더하기 위해서 추가함
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[N]) % 1000000000)