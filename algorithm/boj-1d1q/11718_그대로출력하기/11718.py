import sys
sys.stdin = open("11718.txt", 'r')

while 1:
    s = sys.stdin.readline().replace("\n", "")
    if not s:
        break
    print(s)