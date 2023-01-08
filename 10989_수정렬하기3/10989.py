import sys
sys.stdin = open("10989.txt", 'r')

N = int(sys.stdin.readline())
temp = [0] * (N + 1)
cnt = []
num = []

for _ in range(N):
    n = int(sys.stdin.readline())
    temp[n] += 1
print(temp)