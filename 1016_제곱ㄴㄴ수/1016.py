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
for i in range(2, int((M + 1) ** 0.5)):
    ii = i * i
    for j in range(N, M + 1, ii):
        if not j % ii and sieve[j - N]:
            sieve[j - N] = 0
            cnt += 1