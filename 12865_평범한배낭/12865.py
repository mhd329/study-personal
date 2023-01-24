import sys
sys.stdin = open("12865.txt", 'r')
N, K = map(int, sys.stdin.readline().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    w, v = map(int, sys.stdin.readline().split())
    for j in range(1, K + 1):
        if j >= w:
        # 만약 현재 가방의 여유 공간이 j 일 때
        # 넣으려는 물건의 무게 w 가 충분히 들어갈 수 있다면
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            # 이전것만 넣고 현상유지할건지, 이전것 넣으면서 지금것도 넣을건지
            # 이전것을 넣는데 오히려 w 를 빼는 이유 : 
            # 여유 공간이 j 라는 어떤 숫자인데 그 숫자에서 w 만큼을 뺀다 == w 만큼 넣었다고 가정하는것임
            # 즉 j - w 는 j 에서 w 만큼 넣었을 때 남은 공간을 계산하는것
            # dp[남은 공간] 의 의미는 == dp[그 무게만 넣었을 때의 가치] + 지금것의 가치
        else:
            dp[i][j] = dp[i - 1][j]
            # 더 이상 여유 공간이 없으므로 현상유지로 만족
print(dp[N][K])