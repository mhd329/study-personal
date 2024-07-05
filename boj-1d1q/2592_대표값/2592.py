import sys
sys.stdin = open("2592.txt", 'r')

total = []
for _ in range(10):
    total.append(int(sys.stdin.readline()))

n = 0
fre = 0

for i in total:
    if total.count(i) > fre:
        fre = total.count(i)
        n = i

print(sum(total) // 10)
print(n)