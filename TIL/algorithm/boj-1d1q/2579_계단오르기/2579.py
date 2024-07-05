import sys
sys.stdin = open("2579.txt", 'r')
N = int(sys.stdin.readline())
dp = [0] * 301
st = [0] * 301
for i in range(1, N + 1):
    st[i] = int(sys.stdin.readline())
dp[1] = st[1]
dp[2] = st[1] + st[2]
if N >= 3:
    for i in range(3, 301):
        dp[i] = max(dp[i - 2] + st[i], dp[i - 3] + st[i - 1] + st[i])
    print(dp[N])
elif N == 2:
    print(dp[2])
elif N == 1:
    print(dp[1])