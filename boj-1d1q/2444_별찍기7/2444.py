# 자꾸 출력 형식이 잘못되었다고 함
'''
N = int(input())
m = N - 1
M = N + m
e = M - 1
for i in range(M):
    if i < N:
        for j in range(M):
            if j >= m - i and j <= m + i:
                print("*", end='')
            else:
                print(" ", end='')
        print()
    else:
        for j in range(M):
            if j >= m - (e - i) and j <= m + (e - i):
                print("*", end='')
            else:
                print(" ", end='')
        print()
'''
# 반복문으로 푼 것
N = int(input())
for i in range(1, N):
    print(" " * (N - i) + "*" * (2 * i - 1))
for j in range(N, 0, -1):
    print(" " * (N - j) + "*" * (2 * j - 1))