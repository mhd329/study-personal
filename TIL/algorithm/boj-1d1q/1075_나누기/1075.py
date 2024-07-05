import sys
sys.stdin = open("1075.txt", 'r')

N = list(input())
F = int(input())
    
for i in range(0, 100):
    if i < 10:
        N[-2:] = '0' + str(i)
        # N 의 뒤에서 2번째까지를 str 형식으로 주면 리스트에 문자열당 하나의 원소 단위로 알아서 쪼개져서 들어간다.
        
        # N 이 문자열일때, N = N.replace(N[-2:], '0' + str(i)) 은 이상하게 된다. 왜냐하면 N[-2:] 는 00 인데, 00 은 N이 1000인 경우,
        # N[1] 부터 모두 해당되기 때문에 정확한 자리를 찾을 수가 없다.
    else:
        N[-2:] = str(i)
        
    if int(''.join(N)) % F:
        continue
    else:
        print(''.join(N)[-2:])
        break