import sys
sys.stdin = open("2511.txt", 'r')

A = [*map(int, sys.stdin.readline().split())]
B = [*map(int, sys.stdin.readline().split())]

a = 0
b = 0

win = []

for i in range(10):
    if A[i] > B[i]:
        a += 3
        win.append('A')
    elif A[i] == B[i]:
        a += 1
        b += 1
    else:
        b += 3
        win.append('B')

print(a, b)
if a > b:
    print("A")
elif a == b:
    if len(win) == 0:
        print('D')
    elif win[-1] == 'A':
        print("A")
    else:
        print('B')
else:
    print('B')