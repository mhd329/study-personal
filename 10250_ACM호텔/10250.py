import sys
sys.stdin = open("10250.txt", 'r')

T = int(sys.stdin.readline())

for test_case in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    
    quotient = N // H
    remainder = N % H
    
    if N % H:
        quotient += 1
    else:
        remainder = H
    if not (quotient // 10):
        quotient = '0' + str(quotient)
    
    room_number = str(remainder) + str(quotient)
    
    print(room_number)