N = int(input())
p = [0, 0] + [_ for _ in range(2, N + 1)]
for i in range(2, N + 1):
    if p[i] and i * 2 <= N:
        for j in range(i * 2, N + 1, i):
            p[j] = 0
cnt = 0
end = 2
total = 0
for start in range(2, N + 1):
    if p[start]:
        while total < N and end < N + 1:
            total += p[end]
            end += 1
        if total == N:
            cnt += 1
        total -= p[start]
print(cnt)

# 소수로 시작해야 모든 경우를 다 볼 필요 없이 좀 더 빠르다.
# 소수의 연속합이기 때문에 소수가 아닌 수들은 0 을 더해준다.
# 다른 풀이들보다 내 풀이가 더 깔끔하다고 생각해서 굳이 퍼오지않았다.