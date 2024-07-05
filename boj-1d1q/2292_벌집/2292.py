import sys
sys.stdin = open("2292.txt", 'r')

N = int(sys.stdin.readline())

n = 0
i = 0
j = 0
cnt = 0

while n < N:
    i += j
    n = (6 * i) + 1
    j += 1
    cnt += 1

print(cnt)
'''
N = int(input())
a = 1
b = 1

while N > a:
    a += b * 6
    b += 1
    
print(b)
'''