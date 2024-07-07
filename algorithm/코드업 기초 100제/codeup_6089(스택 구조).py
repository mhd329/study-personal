a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

li = []
li.append(a)

while len(li) < n:
    a *= r
    li.append(a)
    
print(li.pop())