# dp 풀이
import sys
sys.stdin = open("1010.txt", 'r')
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[1][1] = 1
    for i in range(2, M + 1):
        dp[1][i] = dp[1][i - 1] + 1
    for i in range(2, N + 1):
        for j in range(1, M + 1):
            if i > j:
                dp[i][j] = 0
            elif i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
    print(dp[N][M])

# 조합론 풀이
# 공식 => m! // (m - n)!n!
def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m - n))
    print(bridge)

# 쉬운 풀이
case = int(input())

for i in range(case):
    west_site, east_site = map(int, input().split())
    n, m = 1, 1
    for j in range(east_site, east_site-west_site, -1):
        n *= j
    for j in range(1, west_site+1):
        m *= j
    print(n//m)