import sys
sys.stdin = open("1110.txt", 'r')

N = input() # 1
num = N
cnt = 0

while True:
    if int(num) < 10:
        num = '0' + num
    
    n_list = []
    tmp = []
    
    for n in num:
        n_list.append(int(n))

    str_num = str(sum(n_list))
    for n in str_num:
        tmp += n
        
    num = str(n_list.pop()) + tmp.pop()
    cnt += 1
    if int(num) == int(N):
        break

print(cnt)