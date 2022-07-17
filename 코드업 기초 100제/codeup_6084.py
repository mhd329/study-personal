h, b, c, s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

print(f"{(h * b * c * s) / (2 << 22):.1f} MB")