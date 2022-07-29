import sys
sys.stdin = open("2562.txt", 'r')

N = []
for _ in range(9):
    N.append(int(input()))

print(max(N), N.index(max(N)) + 1)