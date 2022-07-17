a, d, n = input().split()

a = int(a)
d = int(d)
n = int(n)

li = []
li.append(a)

while len(li) < n:
    a += d
    li.append(a)
    
print(li.pop())