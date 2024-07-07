'''
a = int(input())

b = input().split()

bli = list(map(int, b))

li = []
for i in range(23):
    li.append(0)
    
for i in range(23):
    for j in bli:
        if (i+1) == j:
            li[i] += 1
for i in li:
    print(i, end = ' ')
'''

n = int(input())

call = input().split()  # 1 4 7 2 5 5 7 9 ... >>> x x x x x x x x x >>> 첫번째가 1번, 두번째가 4번, 세번째가 7번 ... n번째 부른 번호
                        # 0 1 2 3 4 ...                                 == li[1]     == li[4]     ==   li[7] ... 23번까지의 리스트
                        #                                               == li[1] += 1   li[4] += 1     li[7] += 1 ... 23번까지 각 번호당 불린 횟수

li = []

for i in range(23):
    li.append(0)

for i in range(n):
    call[i] = int(call[i])
    
for i in range(n):
    li[call[i]-1] += 1  # [call[i]] 가 리스트의 x 번째
                        # [call[2]] == 4, li[4] >>> 두번째 call이 4번이므로 리스트의 4번에 +1
for i in range(23):
    print(li[i], end = ' ')
    # print(i+1,"번이 불린 횟수")
