users=\
    [
        {'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'},
        {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F'},
        {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'},
        {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F'},
        {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F'}
    ]

# print 뒤에 \ 를 붙여줘야 잘 된다
print\
(
    (
        [ # list()
            users[i]["mail"] for i in range(len(users))
        ]
    )
)

'''
위 코드는
print\
(
    list\
    (
        map(lambda u : u["mail"], users)
    )
)
와 결과값이 같다 ...


map(lambda u : u["mail"], users)
==  for u[i]["mail"], users

'''

'''
그런데
print\
(
    [
        map(lambda u: u["mail"], users)
    ]
)
는 안된다
map 타입으로 결과를 리턴하기 때문이다
list() 식으로 함수를 호출해서 변환하는 과정이 필요하다
그러나 보통은 [] 를 쓰는게 속도면에서는 빠르다 (함수 호출 단계를 생략하기 때문에)

대상 >>> 함수호출 >>> 인식 >>> 변환
대상 >>> 인식 >>> 변환

'''