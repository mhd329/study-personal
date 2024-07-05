import sys
sys.stdin = open("11170.txt", 'r')

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    zero = 0
    
    for i in range(N, M + 1):
        for j in str(i):
            if j == '0':
                zero += 1
    
    print(zero)

# count 써서 풀기
'''
for _ in range(T):
    N, M = map(int, input().split())
    
    zero = 0
    
    for i in range(N, M + 1):
        zero += str(i).count('0')
    
    print(zero)
'''