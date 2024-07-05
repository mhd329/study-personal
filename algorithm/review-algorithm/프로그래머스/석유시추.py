# vertical = set()

# def dfs(x, y, land):
#     global cnt
#     if (x > max_x - 1 or x < 0) or (y > max_y - 1 or y < 0):
#         return False
#     if not land[x][y]:
#         return False
#     vertical.add(y)
#     land[x][y] = 0
#     cnt += 1
#     dfs(x - 1, y, land)
#     dfs(x, y + 1, land)
#     dfs(x + 1, y, land)
#     dfs(x, y - 1, land)
#     return True

# def solution(land):
#     oil_vertical = []
#     res = {}
#     global vertical
#     global max_x
#     global max_y
#     global cnt
#     max_x = len(land)
#     max_y = len(land[0])
#     cnt = 0
#     for i in range(max_x):
#         for j in range(max_y):
#             if land[i][j]:
#                 cnt = 0
#                 dfs(i, j, land)
#                 oil_vertical.append((cnt, list(vertical)))
#                 vertical = set()
    
#     for oil, vertical in oil_vertical:
#         for point in vertical:
#             if point not in res:
#                 res[point] = oil
#             else:
#                 res[point] += oil
    
#     return max(res.values())
