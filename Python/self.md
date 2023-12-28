# self ?

클래스를 만들 때 생성자 혹은 다른 멤버함수에 첫 번째 인자로 보통 self를 쓴다.

파이썬 외의 다른 언어에서도 this라는 이름으로 쓰여지는 이 self에 대해 알아보고자 한다.

------

```python
class Test:
    def func1():
        print("func1() 실행됨")
    def func2(self):
        print(self)
        print(id(self))

test_obj = Test()

print(test_obj.func1())
# >>> TypeError: Test.func1() takes 0 positional arguments but 1 was given
```



- Test 클래스를 정의하고 있다.
- Test 클래스 내부에는 두 개의 멤버함수가 있다.
  - func1 에는 아무 인자도 주어지지 않는다.
  - func2 에는 self만 주어졌다.
- 객체를 만들고 객체의 func1 멤버함수를 print 했다.
  - 0개의 positional arguments를 가지는데 한 개가 주어졌다고 한다!
  - 메서드의 첫 번째 인자로 인스턴스가 전달됐기 때문이다.
  - 나는 생성자가 있을 때를 생각하면서 이해했다. 즉 인스턴스를 만들 때 만들어질 객체인 자기 자신에 대해 정의해야 하므로, 자기 자신이 self 에 전달된다.



```python
class Test:
    def func1():
        print("func1() 실행됨")
    def func2(self):
        print(self)
        print(id(self))

test_obj = Test()

# 1
print(test_obj.func2())
# <__main__.Test object at 0x0000020183A6FFA0>
# 2205526982560
# None

# 2
print(id(test_obj))
# 2205526982560
```



- 이번에는 func2와 test_obj의 id를 print 해보았다.
  - self를 그대로 출력한다.
    - self는 Test 클래스의 인스턴스이다.
  - self의 메모리주소를 출력한다.
  - test_obj의 주소와 같은 것을 확인할 수 있다.
  - 즉 test_obj가 self로 주어졌다.



- 방법을 바꿔서 이번에는 인스턴스가 아닌 클래스 자체의 이름으로 멤버함수들을 호출해보자.



```python
# 1
print(Test.func1())
# func1() 실행됨
# None

# 2
print(Test.func2())
# TypeError: Test.func2() missing 1 required positional argument: 'self'
```



- 앞의 경우에서는 인스턴스를 생성한 다음 그 인스턴스로 함수들을 불러왔지만 이번에는 그러지 않았다.
- 생성된 인스턴스가 없기 때문에 새로 속성을 정의할 인스턴스가 없으므로 self도 주어지지 않았다.
  - self를 받지 않는 func1 멤버함수는 정상적으로 작동하였다.
  - self를 받는 func2 멤버함수는 제대로 작동되지 않았다.