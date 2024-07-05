N = int(input())

f = [0, 1]

i = 0
while i < N:
    n1 = f.pop() # 1
    n2 = f.pop() # 0
    m = n1 + n2
    f.append(n1)
    f.append(m)
    i += 1
print(f[-2])