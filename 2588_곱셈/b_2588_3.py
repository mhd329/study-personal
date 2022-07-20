a = input()
b = input()
tmp = ""
b_list = list(b)
b_list.reverse()
b_reverse = tmp.join(b_list)

for i in b_reverse:
    print(int(a)*int(i))
    
print(int(a)*int(b))