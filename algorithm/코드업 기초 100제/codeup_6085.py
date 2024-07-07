w, h, b = input().split()

w = int(w)
h = int(h)
b = int(b)

print(f"{(w * h * b) / ((2 << 22)):.2f} MB")