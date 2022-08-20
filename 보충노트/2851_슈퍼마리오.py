import sys
sys.stdin = open("2851_슈퍼마리오.txt", 'r')

scr = 0

for _ in range(10):
    scr_pre = int(sys.stdin.readline())
    scr += scr_pre
    if scr > 100:
        scr = (scr if abs(100 - (scr)) <= abs(100 - (scr - scr_pre)) else scr - scr_pre)
        break
print(scr)