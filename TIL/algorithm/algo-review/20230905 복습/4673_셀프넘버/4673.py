n = 1
l = []
while n <= 10000:
    m = 0
    for i in str(n):
        m += int(i)
    l.append(n + m)
    if n not in l:
        print(n)
    n += 1
