alphabet_ord = ord(input())

for i in range(alphabet_ord - 96):
    print(chr(i+97), end = " ")

# 다른 풀이

'''
c = ord(input())
t = ord('a')
while t<=c :
    print(chr(t), end=' ')
    t += 1
'''