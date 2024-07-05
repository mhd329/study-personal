import sys
sys.stdin = open("9012.txt", 'r')
T = int(sys.stdin.readline())
for _ in range(T):
    cnt = 0
    s = [*sys.stdin.readline().strip()]
    while s:
        if s.pop() == ')':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    else:
        if cnt != 0:
            print("NO")
        else:
            print("YES")