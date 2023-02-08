# 1차 시도
# 시간 초과
'''
N, M = map(int, input().split())
arr = []
cnt = 0
for i in range(2, M + 1):
    if i ** 2 > M:
        break
    arr.append(i ** 2)
for j in range(N, M + 1):
    for k in arr:
        if j >= k and not (j % k):
            break
    else:
        cnt += 1
print(cnt)
'''

# 2차 시도
# 메모리 초과
'''
N, M = map(int, input().split())
p = [0, 1] + [_ for _ in range(2, M + 1)]
cnt = M
for i in range(2, M + 1):
    for j in range(i * i, M + 1, i * i):
        if p[j]:
            p[j] = 0
            cnt -= 1
print(cnt)
'''

# 3차 시도
# 시간 초과
'''
N, M = map(int, input().split())
cnt = 0
for i in range(N, M + 1):
    if i > 3:
        for j in range(2, int(i**0.5) + 1):
            if not i % j ** 2:
                break
        else:
            cnt += 1
    else:
        cnt += 1
print(cnt)
'''

# 4차 시도
# 시간, 메모리를 모두 해결했다고 생각했지만 정작 답이 틀렸다.
'''
N, M = map(int, input().split())
sieve = [_ for _ in range(N, M + 1)]
cnt = 0
total = M - N + 1
for i in range(N, M + 1):
    root_i = i ** 0.5
    if int(root_i) > 1 and not i % root_i:
        if sieve[i - N]:
            for j in range(i - N, M - N + 1, i):
                if sieve[j]:
                    sieve[j] = 0
                    cnt += 1
print(total - cnt)
'''

# 5차 시도
N, M = map(int, input().split())
sieve = [_ for _ in range(N, M + 1)]
cnt = 0
total = M - N + 1
for i in range(2, int((M ** 0.5) + 1)):
    i *= i
    for j in range((int((N - 1) // i) + 1) * i, M + 1, i):
        if sieve[N - j]:
            sieve[N - j] = 0
            cnt += 1
print(total - cnt)
# for 문의 시작조건이면서 그것이 동시에 제곱수임
# 식이 (int(N // i) + 1) * i 이고 N 이 8 인 경우와 같이 N 이 제곱수로 나눠지는 수로 시작하면 자기 자신은 제외하고 계산이 시작됨
# 그래서 자기 자신에서 1 을 뺀 값부터 계산해야 자기 자신도 계산이 됨