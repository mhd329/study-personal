# 수정 전 코드

import sys
sys.stdin = open("9461.txt", 'r')

'''
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    for i in range(6, N + 1):
        dp[i] = dp[i - 1] + dp[i - 5]
    else:
        dp = [0] * 6
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 2
    print(dp[N])
'''

# 수정 코드

'''
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    for i in range(6, N + 1):
        dp[i] = dp[i - 1] + dp[i - 5]
    print(dp[N])
'''

# 두 번째 수정 코드

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    for i in range(4, N + 1):
        dp[i] = dp[i - 3] + dp[i - 2]
    print(dp[N])