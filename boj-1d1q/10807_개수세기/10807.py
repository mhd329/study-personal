import sys
sys.stdin = open("10807.txt", 'r')

N = int(sys.stdin.readline())
n = [*map(int, sys.stdin.readline().split())]
v = int(sys.stdin.readline())
num = 0

for i in n:
    if v == i:
        num += 1

print(num)