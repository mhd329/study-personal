import sys
sys.stdin = open("2751.txt", 'r')

N = int(sys.stdin.readline())
num = []

for _ in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()

print(*num, sep = "\n")

# 너무 어렵게 생각해서 시간초과가 나왔다...