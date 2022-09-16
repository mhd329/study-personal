N = int(input())

def star(n):
    if n == 1:
        return '*'
    else:
        star_set = []
        star_print = star(n // 3)
        
        for star_ in star_print:
            star_set.append(star_ * 3)
        
        for star_ in star_print:
            star_set.append(star_ + ' ' * (n // 3) + star_)
        
        for star_ in star_print:
            star_set.append(star_ * 3)
        
        return star_set

for i in star(N):
    print(i, end='\n')