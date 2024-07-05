def con ():
    gen = [] # 생성자로 생성된 것들
    nums = [] # 전체 수
    
    for i in range(1, 10001):
        nums.append(i)
        gen_num = 0
        for char in str(i):
            gen_num += int(char)
        gen_num += i
        gen.append(gen_num)
    
    res = sorted(list(set(nums) - set(gen)))
    
    for j in res:
        print(j)

con()