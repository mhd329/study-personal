# Class

오늘은 파이썬의 클래스를 살펴보자.

------

클래스 :

- 사용자가 정의한 속성들이 있는 특정 객체들을 만들기위한 설계도
- 파이썬의 클래스는 자신만의 네임스페이스를 가진다.
- 클래스의 네임스페이스를 확인하고 싶다면 클래스이름.__dict__ 로 확인할 수 있다.
  - Account.__dict__



```python
class Account:
    total_accounts = 0
    def __init__(self, client_name:str):
        self.client_name = client_name
        Account.total_accounts += 1
    def __del__(self):
        Account.total_accounts -= 1
```



- 은행 계좌를 개설하는 클래스를 만들었다.
  - Account 클래스는 total_accounts라는 클래스 변수를 가진다.
  - 생성자 init에 의해 인스턴스가 생성될 때 고객의 이름이 문자열 타입으로 들어가야 한다.
  - 객체가 생성될 때 total_accounts는 1씩 증가한다.
  - 객체가 삭제될 때 total_accounts는 1씩 감소한다.
- 이제 실제로 어떻게 작동하는지 예시 코드들을 써 가며 분석해보자.



```python
james = Account("james")

# 1
print("Account.total_accounts :", Account.total_accounts)
# >>> Account.total_accounts : 1

# 2
print("james.client_name :", james.client_name)
# >>> james.client_name : james

# 3
print("Account.client_name :", Account.client_name)
# >>> AttributeError: type object 'Account' has no attribute 'client_name'
```



- james라는 고객의 계좌 객체를 새로 만들었다.
  - \# 1 에서 클래스 변수 total_accounts는 1이 증가했다.
  - \# 2 에서 james.client_name이라는 인스턴스 변수에는 계좌 주인의 이름을 나타내는 "james" 문자열 객체가 할당되어 있다.
  - \# 3 에서 Account 타입은 client_name이라는 어트리뷰트가 없다고 한다.
    - 클래스가 인스턴스화 될 때 생성자에 의해 client_name이라는 인스턴스 변수가 생기게 된다.
    - 클래스 이름으로 접근했기 때문에 아직 생성되지 않은 client_name에 대해서 찾을 수 없다고 하는 것이다.



```python
print("Account().client_name :", Account().client_name)
# >>> TypeError: Account.__init__() missing 1 required positional argument: 'client_name'
```



- Account() 로 객체를 생성할 때는 반드시 생성자에서 정해놓은 형식의 매개변수가 같이 주어져야 한다.



```python
print("dir(james) :", dir(james))
'''
>>> dir(james) : [
'__class__', '__del__', '__delattr__', '__dict__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
'__lt__', '__module__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', '__weakref__', 'client_name', 'total_accounts'
]
'''
```



- dir() 내장 함수는 객체를 인자로 넣어주면 그 객체가 가지고 있는 변수나 메서드를 나열해준다.
- 맨 마지막 두 개 항목을 보면 인스턴스 변수와 클래스 변수가 있음을 알 수 있다.



```python
print("dir(Account) :", dir(Account))
'''
>>> dir(Account) : [
'__class__', '__del__', '__delattr__', '__dict__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
'__lt__', '__module__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', '__weakref__', 'total_accounts'
]
'''
```



- 위의 경우 클래스 이름으로 객체의 선언 없이 조회했기 때문에 인스턴스 변수 client_name은 빠져 있다.



```python
print("james.total_accounts :", james.total_accounts)
# >>> james.total_accounts : 1

del james

print("Account.total_accounts :", Account.total_accounts)
# >>> Account.total_accounts : 0
```



- james 객체로 클래스 변수를 조회했다.
  - james 객체의 인스턴스 변수 중 total_accounts를 찾는다.
  - james 객체에는 total_accounts라는 인스턴스 변수가 없기 때문에 원본 클래스인 Account에서 클래스 변수 total_accounts를 찾는다.
  - 즉, 출력된 total_accounts는 james 객체의 것이 아니라 클래스 변수 total_accounts의 현재 값이다.
- james 객체를 삭제하고 클래스 변수를 조회했다.
- 객체가 삭제됐기 때문에 클래스 변수도 하나 감소하여 0이 되었다.



```python
lee = Account("lee")

# 1
print("Account :", Account)
# >>> Account : <class '__main__.Account'>

# 2
print("lee :", lee)
# >>> lee : <__main__.Account object at 0x000002826201FFD0>
```



- 새로운 계좌 객체 "lee" 를 만들었다.

  - \# 1 에서 클래스 이름으로 print하면 최상위 환경 __main__에 속해있는 class인 "Account" 라고 나온다.

  - \# 2 에서 인스턴스의 이름으로 print하면 최상위 환경

     

     __main__에 속해있는 class인 "Account" 객체라고 나오고 메모리 주소가 나온다.

    - 인스턴스의 이름을 print 했을 때 메모리 주소 대신 다른 정보를 출력하게 하고 싶다면 매직 메서드 __str__, __repr__ 등을 사용하면 된다.
    - 아래에 매직 메서드 __str__, __repr__의 차이에 대한 아주 재미있는 포스팅이 있다.
    - 차이에 대해 여기서 말할수도 있지만 그렇게 되면 저 사람의 블로그에 들어가보지 않을 것 같으니 여기에는 쓰지 않겠다.
      - 참조 : https://shoark7.github.io/programming/python/difference-between-__repr__-vs-__str__
        - 링크 안되는 경우 [여기](https://mhd329.tistory.com/24)에서 맨 아래의 링크로 접속

---

**이런 나무위키식 학습 좋아요~!!**

