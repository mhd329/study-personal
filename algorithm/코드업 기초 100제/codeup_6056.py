a, b = input().split()

# print((bool(int(a)) and (not bool(int(b)))) or ((not bool(int(a))) and bool(int(b))))

print(bool(int(a)) != bool(int(b)))