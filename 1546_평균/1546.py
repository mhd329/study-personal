import sys
sys.stdin = open("1546.txt", 'r')

N = int(input())
sub = list(map(int, input().split()))

M = max(sub)

for score in range(len(sub)):
    sub[score] = (sub[score] / M) * 100

print(sum(sub) / len(sub))