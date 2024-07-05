N = int(input())

def print_star(n):
    if n == 1:
        return ['*']
    
    stars = print_star(n // 3)
    temp_star = []
    
    for star in stars:
        temp_star.append(star * 3)
        
    for star in stars:
        temp_star.append(star + ' ' * (n // 3) + star)
        
    for star in stars:
        temp_star.append(star * 3)
        
    return temp_star

print('\n'.join(print_star(N)))