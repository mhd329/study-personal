a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

li = []
li.append(a)

while len(li) < n:
    a *= m
    a += d
    li.append(a)
    
print(li.pop())