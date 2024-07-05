'''
import sys
sys.stdin = open("2720.txt", 'r')

T = int(sys.stdin.readline())

for _ in range(T):
    answer = []
    C = int(sys.stdin.readline())
    a, b = divmod(C, 25)
    answer.append(a)
    b, c = divmod(b, 10)
    answer.append(b)
    c, d = divmod(c, 5)
    answer.append(c)
    answer.append(d)
    print(*answer)
'''
# 더 짧은 풀이
n = int(input())

for _ in range(n):
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')
		money = money%i