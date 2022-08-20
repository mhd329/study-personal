import sys
sys.stdin = open("9095.txt", 'r')

T = int(sys.stdin.readline())

dp = [0] * 11
dp[1], dp[2], dp[3] = 1, 2, 4

for test_case in range(T):
    n = int(sys.stdin.readline())
    
    for i in range(4, 11):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    
    print(dp[n])