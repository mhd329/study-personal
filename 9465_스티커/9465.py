import sys
from pprint import pprint
sys.stdin = open("9465.txt", 'r')
T = int(sys.stdin.readline())
for testcase in range(T):
    N = int(sys.stdin.readline())
    sticker = []
    dp = [[0] * (N + 1) for _ in range(3)]
    for _ in range(2):
        sticker.append([*map(int, sys.stdin.readline().split())])
    '''for i in range(2):
        for j in range(N):
            if j >= 2:
                dp[i][j] = sticker[i][j] + sticker[i + 1][j - 1] + dp[i][j - 2]
            elif j == 1:
                dp[i][j] = sticker[i][j] + sticker[i + 1][j - 1]
            else:
                dp[i][j] = sticker[i][j]'''
    for i in range(1, 3):
        for j in range(1, N + 1):
            if i == 1:
                if j < 3:
                    dp[i][j] = sticker[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 2][j] + sticker[i - 1][j - 1]
            else:
                if j == N:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1] + sticker[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1] + sticker[i - 1][j - 1]
    pprint(dp)