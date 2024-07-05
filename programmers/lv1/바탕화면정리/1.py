# 내 풀이

def solution(wallpaper):
    x = len(wallpaper)
    y = len(wallpaper[0])
    lx = x - 1
    ly = y - 1
    rx = 0
    ry = 0
    for i in range(x):
        if "#" in wallpaper[i]:
            lx = min(lx, i)
            rx = max(rx, i + 1)
    for i in range(x):
        for j in range(y):
            if wallpaper[i][j] == '#':
                ly = min(ly, j)
                ry = max(ry, j + 1)
    answer = [lx, ly, rx, ry]
    return answer

# 다른 사람 풀이

'''
def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]
'''

'''
def solution(wallpaper):
    x = []
    y = []
    for i, row in enumerate(wallpaper):
        for j, col in enumerate(row):
            if col == '#':
                x.append(i)
                y.append(j)
    return [min(x), min(y), max(x)+1, max(y)+1]
'''