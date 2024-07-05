import sys
sys.stdin = open("2581.txt", 'r')

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

p = set()
i = 2

while M <= N:
    while i <= M:
        if M % i:
            i += 1
            if M == i:
                p.add(M)
                break
        else:
            break
    if M == 2:
        p.add(M)
    M += 1
    i = 2
    
if len(p):
    print(sum(p))
    print(min(p))
else:
    print(-1)

# 백준 다른풀이
'''
import sys 
input = sys.stdin.readline
M = int(input())
N = int(input())

li = []
for n in range(M, N+1):
    if n > 1 :
        for i in range(2, n):  
            if not n % i: break
        else:  li += [n]
if len(li): print(sum(li), li[0], sep='\n')
else: print(-1)
'''
'''
m=int(input())
n=int(input())
list=[]
for i in range(m,n+1):
    f=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                f+=1
                break
        if f==0:
            list.append(i)
if len(list)>0:
    print(sum(list))
    print(min(list))
else:
    print(-1)  
'''