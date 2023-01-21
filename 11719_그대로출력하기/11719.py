import sys
sys.stdin = open("11719.txt", 'r')

while 1:
    s = sys.stdin.readline()
    if s:
        print(s, end='')
    else:
        break