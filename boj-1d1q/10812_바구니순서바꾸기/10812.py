import sys
sys.stdin = open("10812.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
basket = [0] + [i for i in range(1, N + 1)]
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    mid_to_rear = basket[k:j + 1]
    front_to_mid = basket[i:k]
    basket[i:j + 1] = mid_to_rear + front_to_mid
print(*basket[1:])