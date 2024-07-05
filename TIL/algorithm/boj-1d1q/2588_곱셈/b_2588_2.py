a = input()
b = input()
b_reverse = ""
for s in b:
    b_reverse = s + b_reverse

for i in b_reverse:
    print(int(a)*int(i))
    
print(int(a)*int(b))

