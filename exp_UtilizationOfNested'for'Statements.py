# 행렬을 일차원으로 바꾸는 코드
# https://mingrammer.com/introduce-comprehension-of-python/

matrix =\
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]
#flatten = [e for r in matrix for e in r]
#flatten = [ (e) / for r in matrix / for e in r]
#                      r = [1~4] ...     e = 1,2,3,4 ...   
#                                        e 를 리스트에 넣어라
# 1. e 를 넣은 리스트를 만들어라 ( e 는 무엇인가 ? )
# 2. matrix 안의 각 원소 r 에 대하여
# 3. r 안의 각 원소 e 를

# 위 코드는 아래와 같은 결과를 낸다

flatten = []
for r in matrix:
    for e in r:
        flatten.append(e)

print(flatten)
