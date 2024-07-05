a = 123

b = a # a의 주소값을 b도 참조
print('***************')
print("a의 주소는",id(a))
print("b의 주소는",id(b))

a = a + b
print('***************')
print("a와 b가 더해진 a의 주소는",id(a))
print("b의 주소는",id(b))

a = a + b
print('***************')
print("a와 b가 더해진 a의 주소는",id(a))
print("b의 주소는",id(b))

###########

c = 123
print('***************')
print("c의 주소는",id(c))

# a += b 라는 연산을 할 때마다 a가 가리키는 주소값은 달라진다.
# 또한 c와 b의 주소값, 그리고 a의 맨 처음 주소값이 모두 같은 것을 확인할 수 있는데,
# 그 이유는 파이썬은 모든 것이 객체이기 때문에 인터프리터가 작동했을 때 내부적으로 모든 값(객체)에 대해서 주소값을 부여해 놓기 때문이 아닌가 싶다.
# 따라서 정수 123 이라는 객체는 고정된 어떤 주소값을 가지기 때문에 123이라는 주소값이 담기는 변수들의 id는 모두 같을 수 밖에 없다.