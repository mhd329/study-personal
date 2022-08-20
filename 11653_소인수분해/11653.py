N = int(input())

i = 2
pf = []

while N > 1:
    if N % i:
        i += 1
        continue
    N //= i
    pf.append(i)

if len(pf):
    for i in pf:
        print(i)