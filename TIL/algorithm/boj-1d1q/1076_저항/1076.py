import sys
sys.stdin = open("1076.txt", 'r')

ohm =\
{
"black" : '0',
"brown" : '1',
"red" : '2',
"orange" : '3',
"yellow" : '4',
"green" : '5',
"blue" : '6',
"violet" : '7',
"grey" : '8',
"white" : '9'
}

total = ''

for i in range(3):
    if i == 2:
        total = int(total) * (10 ** int(ohm[sys.stdin.readline().rstrip()]))
    else:
        total += ohm[sys.stdin.readline().rstrip()]

print(total)