def solution(x, y, n):
    # y회 만큼 반복하면 y가 되는 경우가 있기 때문에 y+1을 해야함.
    dp = [y + 1] * (y + 1)
    dp[x] = 0
    for i in range(x, y + 1):
        if i + n <= y:
            dp[i + n] = min(dp[i] + 1, dp[i + n])
        if i * 2 <= y:
            dp[i * 2] = min(dp[i] + 1, dp[i * 2])
        if i * 3 <= y:
            dp[i * 3] = min(dp[i] + 1, dp[i * 3])
    if dp[-1] == y + 1:
        return -1
    else:
        return dp[-1]