import sys
sys.stdin = open("2167_2차원배열의합.txt", 'r')

N, M = map(int, sys.stdin.readline().split())

arr = []

for _ in range(N):
    arr.append([*map(int, sys.stdin.readline().split())])

K = int(sys.stdin.readline())

for _ in range(K):
    total = 0
    i, j, x, y = map(int, sys.stdin.readline().split())
    
    for r in range(i - 1, x):
        for c in range(j - 1, y):
            total += arr[r][c]
    
    print(total)