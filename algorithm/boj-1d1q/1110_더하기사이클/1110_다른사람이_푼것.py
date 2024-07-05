import sys
sys.stdin = open("1110.txt", 'r')

N = input() # 26
num = N
result = 0
while True:
    if len(num) == 1:
        num = "0" + num
    sum_ = str(int(num[0]) + int(num[1])) # 8
    num = num[-1] + sum_[-1] # 68
    result += 1
    if int(num) == int(N):
        break
print(result)