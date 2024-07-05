import sys
sys.stdin = open("10811.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
basket = [0] + [i for i in range(1, N + 1)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    cnt = j - i
    for k in range(1, cnt + 1):
        basket.insert(i, basket.pop(i + k))
print(*basket[1:])

# 왜 이걸 생각 못했나 싶은 코드

'''
N, M = map(int,input().split())
basket = [n for n in range(1,N+1)]
for m in range(M):
    i, j = map(int,input().split())
    part = list(reversed(basket[i-1:j]))
    basket[i-1:j] = part
print(*basket)
'''