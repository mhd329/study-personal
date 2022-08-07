import sys

sys.stdin = open("2711.txt", 'r')

T = int(sys.stdin.readline())

for test_case in range(T):
    i, word = sys.stdin.readline().split()
    wl = []
    
    for s in word:
        wl.append(s)
        
    del wl[int(i) - 1]
    print(''.join(wl))