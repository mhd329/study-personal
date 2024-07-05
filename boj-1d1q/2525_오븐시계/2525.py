h, m1 = map(int, input().split())
m2 = int(input())

m3 = m1 + m2

while True:
    if m3 < 60:
        break
    m3 -= 60
    h += 1
    if h >= 24:
        h = 0
        
print(h, m3)