import sys
sys.stdin = open("2902.txt",'r')

input_ = sys.stdin.readline().rstrip()

for i in input_:
    if ord(i) >= 64 and ord(i) <= 90:
        print(i, end='')