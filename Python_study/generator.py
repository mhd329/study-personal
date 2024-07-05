def gn ():
    
    yield 1
    yield 2
    yield 3
    
gnn1 = gn ()

print(gnn1)
print(gnn1) # next 가 실행되기 전까지 그 단계에서 대기한다.

print(type(gnn1))

print("next gnn is (first) :",next(gnn1))
print("gnn :",gnn1)
print(type(next(gnn1))) # next 가 실행된것으로 친다 >>> yield 2 는 생략이 되어버렸다.
print("next gnn is (second) :",next(gnn1))
print("gnn :",gnn1) # gnn 의 주소값은 변하지 않는다.
# print("next gnn is (third) :",next(gnn1))
# print(type(next(gnn1)))
# print(next(gnn1))


####################


gnn2 = gn ()

print(gnn2)

print(gnn1 is gnn2) # 서로 다른 generator 이며 따로 동작한다


####################


def infinite_gn():
    
    cnt = 0
    
    while 1: # 영원히 동작한다
        cnt += 1
        yield cnt # 영원히 새로운 숫자가 나옴

gnn3 = infinite_gn()

print(f"{next(gnn3)}번째 next :",next(gnn3)) # 1번째 next : 2
print(f"{next(gnn3)}번째 next :",next(gnn3)) # 3번째 next : 4
print(f"{next(gnn3)}번째 next :",next(gnn3)) # 5번째 next : 6
print(f"{next(gnn3)}번째 next :",next(gnn3)) # 7번째 next : 8
print(f"{next(gnn3)}번째 next :",next(gnn3)) # 9번째 next : 10


####################


def gn_3_1 ():
    l = [1, 2, 3]
    for i in l:
        yield i

# gn3_1 = [gn_3_1 ()]
gn3_1 = gn_3_1 ()
gn3_2 = gn_3_1 ()

print([gn3_1])
print(list(gn3_1))
print(list(gn3_1))

print([gn3_2])
print(*gn3_2)
print(list(gn3_2))
print(list(gn3_2))

print(list(gn3_2))

# 아래와 같이 for 문을 쓰지 않고 간략하게 쓸 수 있다.

def gn_3_2 ():
    l = [1, 2, 3]
    yield from l

gen = gn_3_2 ()
print(list(gen))