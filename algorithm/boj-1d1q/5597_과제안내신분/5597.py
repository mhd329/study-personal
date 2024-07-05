import sys
sys.stdin = open("5597.txt", 'r')
n = [0]
n += [False for i in range(30)]

for _ in range(28):
    i = int(sys.stdin.readline())
    n[i] = True

for j in range(1, 31):
    if n[j] == False:
        print(j)

# 더 짧은 코드
'''
arr = []
for i in range(28):
    arr.append(int(input()))

for i in range(1, 31):
    if i not in arr:
        print(i)
'''