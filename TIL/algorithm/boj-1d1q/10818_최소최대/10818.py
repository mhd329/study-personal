import sys
sys.stdin = open("10818.txt", 'r')

N = int(input())
numbers = list(map(int, input().split()))

min_num = numbers[0]
max_num = numbers[0]
cycle = 0

while cycle < N:
    if min_num > numbers[cycle]:
        min_num = numbers[cycle]
    if max_num < numbers[cycle]:
        max_num = numbers[cycle]
    cycle += 1

print(min_num, max_num)