N = int(input())
A = [*map(int, input().split())]
dp = list(A)
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], A[i] + dp[j])
print(max(dp))
# 리스트를 돌면서 나보다 작은 애들만 더하면 돈다.
# 그리고 max를 안해줘서 틀렸는데 그 이유는,
# 5 3 8 과 같은 경우 5 + 8이 더 큰데 그 이후에 3 + 8로 바뀌어버리기 때문이다.
