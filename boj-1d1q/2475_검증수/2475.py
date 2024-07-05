import sys
sys.stdin = open("2475.txt", 'r')

N = [*map(int, sys.stdin.readline().split())]
res = 0
for n in N:
    res += n ** 2
res %= 10
print(res)