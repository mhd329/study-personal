import sys
sys.stdin = open("10733.txt", 'r')

K = int(input())
nums = []
for input_ in range(1, K + 1):
    N = int(input())
    
    if N == 0:
        nums.pop()
    else:
        nums.append(N)
        
print(sum(nums))