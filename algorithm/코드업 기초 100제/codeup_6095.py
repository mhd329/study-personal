d=[]         

for i in range(19):
    d.append([])
    for j in range(19):
        d[i].append(0)

        
n = int(input()) # 바둑알 놓은 개수
for i in range(n) :
    x, y = input().split()
    d[int(x)-1][int(y)-1] = 1
    
for i in range(19) :
    for j in range(19) : 
        print(d[i][j], end=' ')
    print()
