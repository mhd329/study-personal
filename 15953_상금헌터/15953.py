import sys
sys.stdin = open("15953.txt", 'r')

T = int(sys.stdin.readline())

competition_a = [0] * 101
competition_b = [0] * 65

for i in range(1, 101):
    if i == 1:
        competition_a[i] = 5000000
    if competition_a[i] == 0:
        if i < 4:
            competition_a[i] = 3000000
        elif i < 7:
            competition_a[i] = 2000000
        elif i < 11:
            competition_a[i] = 500000
        elif i < 16:
            competition_a[i] = 300000
        elif i < 22:
            competition_a[i] = 100000

j = 0
while j < 5:
    for k in range(2 ** j, 2 ** (j + 1)):
        competition_b[k] = 5120000 // (2 ** j)
    j += 1

for test_case in range(T):
    a, b = map(int, sys.stdin.readline().split())
    
    print(competition_a[a] + competition_b[b])