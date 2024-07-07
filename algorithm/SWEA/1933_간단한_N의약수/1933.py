# import sys
# sys.stdin = open("input.txt", 'r')

n = int(input())
aliquot = []

for i in range(1, n + 1):
    if n % i == 0:
        aliquot.append(i)
        aliquot.sort()
        
for i in aliquot:
    print(i, end = ' ')