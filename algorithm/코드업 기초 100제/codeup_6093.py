'''
n = int(input())

call = input().split()

for i in range(n):
    call[i] = int(call[i])

reverse_call = call[::-1]

for i in reverse_call:
    print(i, end = ' ')
'''
'''
n = int(input())

call = input().split()

for i in range(n-1, -1, -1):
    print(call[i], end = ' ')
'''

n = int(input())

call = input().split()

i = n-1
while i >= 0:
    print(call[i], end = ' ')
    i -= 1
