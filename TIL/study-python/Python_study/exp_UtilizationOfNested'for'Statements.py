# 행렬을 일차원으로 바꾸는 코드
# https://mingrammer.com/introduce-comprehension-of-python/

matrix_2d =\
[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

flatten_2d = [e for r in matrix_2d for e in r]

# flatten_2d = [ (e) / for r in matrix_2d / for e in r]
#                      r = [1~4] ...     e = 1,2,3,4 ...   
#                                        e 를 리스트에 넣어라
# 1. e 를 넣은 리스트를 만들어라 ( e 는 무엇인가 ? )
# 2. matrix_2d 안의 각 원소 r 에 대하여
# 3. r 안의 각 원소 e 를

# 위 코드는 아래와 같은 결과를 낸다

'''
flatten_2d = []
for r in matrix_2d:
    for e in r:
        flatten_2d.append(e)

print(flatten_2d)
'''

# 그렇다면 응용하여 3차원 행렬을 단순화하는 코드를 만들어보자

matrix_3d =\
[
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [11,12,13],
        [14,15,16],
        [17,18,19]
    ],
    [   
        [21,22,23],
        [24,25,26],
        [27,28,29]
    ]
]

# 가로 3, 세로 3, 3 층의 행렬

# w = 1,2,3 ...
# v = [[1,2,3] ... ]
# h = [v1,v2,v3 ... ]

flatten_3d = [w for h in matrix_3d for v in h for w in v]
print(flatten_3d)

'''
flatten_3d = []
for h in matrix_3d:
    for v in h:
        for w in v:
            flatten_3d.append(w)
            
print(flatten_3d)
'''