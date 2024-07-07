import sys
sys.stdin = open("17413.txt", 'r')

S = sys.stdin.readline().rstrip()

flag = False
char = ""
temp = ""
temp2 = []

if '<' in S:
    for s in S:
        if s == '<':
            temp = temp.split()
            for t in temp:
                temp2.append(t[::-1])
            temp = ' '.join(temp2)
            char += temp
            temp = ""
            temp2 = []
            flag = True
        if flag:
            char += s
        elif not flag:
            temp += s
        if s == '>':
            flag = False
    temp = temp.split()
    for t in temp:
        temp2.append(t[::-1])
        ' '.join(temp2)
    temp = ' '.join(temp2)
    char += temp
    print(char)
else:
    S = S.split()
    for s in S:
        print(s[::-1], end = ' ')