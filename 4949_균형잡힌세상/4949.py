import sys
sys.stdin = open("4949.txt", 'r')

sentence = ['']

while 1:
    ref = True
    ps = []
    sentence = sys.stdin.readline().rstrip()
    if sentence[0] == '.':
        break
    try:
        for s in sentence:
            if ref:
                if s == '(':
                    ps.append(s)
                elif s == ')':
                    if ps[-1] == '(':
                        ps.pop()
                    else:
                        ref = False
                        break
                elif s == '[':
                    ps.append(s)
                elif s == ']':
                    if ps[-1] == '[':
                        ps.pop()
                    else:
                        ref = False
                        break
                else:
                    continue
    except:
        ref = False
    if ref and len(ps) == 0:
        print("yes")
    else:
        print("no")
