# 첫 번째 시도했던 코드
'''
import sys
sys.stdin = open("9465.txt", 'r')
T = int(sys.stdin.readline())
for testcase in range(T):
    N = int(sys.stdin.readline())
    sticker = []
    dp = [[0] * (N + 1) for _ in range(3)]
    for _ in range(2):
        sticker.append([*map(int, sys.stdin.readline().split())])
    for i in range(1, N + 1):
        if i == 1:
            dp[1][i], dp[2][i] = sticker[0][0], sticker[1][0]
        else:
            dp[1][i] = max(dp[2][i - 1] + sticker[0][i - 1], dp[1][i - 1])
            dp[2][i] = max(dp[1][i - 1] + sticker[1][i - 1], dp[2][i - 1])
    print(dp[-1][-1])
'''
# 두 번째 시도했던 코드
import sys
sys.stdin = open("9465.txt", 'r')
T = int(sys.stdin.readline())
for testcase in range(T):
    N = int(sys.stdin.readline())
    sticker = []
    dp = [[0] * (N + 1) for _ in range(3)]
    for _ in range(2):
        sticker.append([*map(int, sys.stdin.readline().split())])
    for i in range(1, N + 1):
        if i == 1:
            dp[1][i], dp[2][i] = sticker[0][0], sticker[1][0]
        else:
            dp[1][i] = max(dp[2][i - 1] + sticker[0][i - 1], dp[1][i - 1])
            dp[2][i] = max(dp[1][i - 1] + sticker[1][i - 1], dp[2][i - 1])
    print(max(dp[1][-1], dp[2][-1]))