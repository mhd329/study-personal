import sys
sys.stdin = open("input.txt", 'r')

n = int(input())

nums = list(map(lambda x : str(x), range(1, n + 1)))

for i in nums:
    sum_369 = (i.count('3') + i.count('6') + i.count('9'))
    if '3' in i:
        print('-' * sum_369, end = ' ')
    elif '6' in i:
        print('-' * sum_369, end = ' ')
    elif '9' in i:
        print('-' * sum_369, end = ' ')
    else:
        print(i, end = ' ')
        
    # i in 3
    # i 있다. ~ 안에 3
    
    # >>> 3 안에 i 있다.
    
    # 3 in i
    # 3 있다. ~ 안에 i
    
    # >>> i 안에 3 있다.
    
    # 왜 자꾸 헷갈리지 '~'