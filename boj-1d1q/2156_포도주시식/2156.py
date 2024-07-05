import sys
sys.stdin = open("2156.txt", 'r')
N = int(sys.stdin.readline())
dp = [0] * (N + 1)
n = [0]
for _ in range(1, N + 1):
    n.append(int(sys.stdin.readline()))
if N == 1:
    print(n[1])
elif N == 2:
    print(n[1] + n[2])
elif N >= 3:
    dp[1] = n[1]
    dp[2] = n[1] + n[2]
    for i in range(3, N + 1):
        dp[i] = max(n[i] + n[i - 1] + dp[i - 3], n[i] + dp[i - 2], dp[i - 1])
        # 계단 오르기 문제와 다르게 dp[i - 1] 이 붙는 이유는
        # 반드시 마지막 잔을 마셔야만 한다 라는 조건이 없기 때문이다.
        # max(dp[i - 1]) 이 선택되는 경우 : 
        # n[1] = 3
        # n[2] = 2
        # n[3] = 1
        # 일 때 dp[3] = n[1] + n[2](dp[2])
        # 즉 마지막 잔을 마시지 않는 경우를 생각하기 위해서 추가함
    print(max(dp))