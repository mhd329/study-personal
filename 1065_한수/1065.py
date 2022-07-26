import sys
sys.stdin = open("1065.txt", 'r')

N = int(input())
cnt = 0

for i in range(1, N + 1):
    tmp = []
    for j in range(1, len(str(i))): # 246
        tmp.append(int(str(i)[j]) - int(str(i)[j-1]))
    if len(list(set(tmp))) != 2:
        cnt += 1

print(cnt)