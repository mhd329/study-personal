import sys
sys.stdin = open("11721.txt", 'r')
s = sys.stdin.readline()
n = len(s) // 10
for i in range(n):
    print(s[i * 10:(i * 10) + 10])
else:
    print(s[n * 10:])

# 더 좋아보이는 풀이
'''
import sys
input = sys.stdin.readline
s = input()
while len(s) > 10:
    print(s[0:10])
    s = s[10:]
print(s)
'''

# 짧으면서 쉽고 좋은 풀이
'''
n = input()
for i in range(0, len(n), 10):
	print(n[i:i+10])
'''