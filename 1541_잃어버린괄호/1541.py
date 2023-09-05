e = input()
e = e.split("-")
i = e.pop(0)
i = sum(map(int, i.split("+")))
for j in e:
    i -= sum(map(int, j.split("+")))
print(i)
