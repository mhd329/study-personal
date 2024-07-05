n = list(map(int, sorted(input().split(), reverse = True)))

if n[0] != n[1] != n[2]:
    prize = n[0] * 100

if n[0] == n[1] == n[2]:
    prize = 10000 + n[0] * 1000

elif n[0] == n[1]:
    prize = 1000 + n[0] * 100
    
elif n[1] == n[2]:
    prize = 1000 + n[1] * 100
    
print(prize)

# 다른사람 코딩

'''
a, b, c = map(int, input().split())

if a == b == c :
  print(10000 + a * 1000)
elif a == b :
  print(1000 + a * 100)
elif a == c :
  print(1000 + a * 100)
elif b == c :
  print(1000 + b * 100)
else :
  print(max(a, b, c) * 100)
'''