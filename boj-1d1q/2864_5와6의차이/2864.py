import sys
sys.stdin = open("2864.txt", 'r')

A, B = map(int, sys.stdin.readline().split())

str_A = str(A)
str_B = str(B)

max_sum = 0
min_sum = 0
A_convert_5_to_6 = 0
B_convert_5_to_6 = 0
A_convert_6_to_5 = 0
B_convert_6_to_5 = 0

if '5' in str_A:
    A_convert_5_to_6 = int(str_A.replace('5', '6'))
else:
    A_convert_5_to_6 = A
    
if '5' in str_B:
    B_convert_5_to_6 = int(str_B.replace('5', '6'))
else:
    B_convert_5_to_6 = B

max_sum = A_convert_5_to_6 + B_convert_5_to_6

if '6' in str_A:
    A_convert_6_to_5 = int(str_A.replace('6', '5'))
else:
    A_convert_6_to_5 = A
    
if '6' in str_B:
    B_convert_6_to_5 = int(str_B.replace('6', '5'))
else:
    B_convert_6_to_5 = B

min_sum = A_convert_6_to_5 + B_convert_6_to_5

print(min_sum, max_sum)

# 완전 헛짓이었다.

'''
a,b=input().split()
amax=a.replace('5','6')
bmax=b.replace('5','6')
amin=a.replace('6','5')
bmin=b.replace('6','5')
print(int(amin)+int(bmin),int(amax)+int(bmax))
'''