# Enum : 열거형

<br>

- 열거형은 고유한 상숫값에 연결된 기호 이름(멤버)의 집합이다.
  - [파이썬 공식 문서](https://docs.python.org/ko/3.9/library/enum.html)에서 설명하고 있음.
- 이 가이드 문서는 아래 문서를 참조하여 작성되었음.
  - https://www.daleseo.com/python-enum/

<br>

---

<br>

- 파이썬 에서의 열거형 클래스 활용

  - 파이썬은 버전 3.4부터 Enum 타입을 지원하고 있다.
  - Enum을 잘 활용하면 인스턴스의 종류를 제한할 수 있기 때문에 견고한 프로그래밍에 도움이 된다.

  ```python
  from enum import Enum
  
  class Color(Enum):
      RED = 1
      BLUE = 2
      GREEN = 3
  ```

  - Enum 타입의 상수 인스턴스는 기본적으로 이름과 값 속성을 가진다.

  ```python
  print(Color.RED.name) # RED
  print(Color.RED.value) # 1
  ```

  - 순회도 가능하다.

  ```python
  for color in Color:
      print(color)
  
  # Color.RED
  # Color.BLUE
  # Color.GREEN
  ```

<br>

---

<br>

- 클래스 방식이 아닌 함수 타입의 활용

  - Enum 클래스를 일반 함수처럼 호출해서 활용할 수 있다.

  ```python
  from enum import Enum
  
  c = Enum("Color", "RED BLUE GREEN")
  
  print(list(c))
  # [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
  ```

<br>

---

<br>

- 값의 자동 할당

  - 중복되지 않는 값들을 자동으로 순차 할당해줄 수도 있다.
  - 또는 `_generate_next_value_()` 메서드를 불러와서 특정 값을 할당할 수도 있다.
    - 아래의 경우는 상수 이름과 동일한 문자열을 그 값으로 할당해준다.
  - 이 때는 `enum` 모듈의 `auto()` 클래스를 사용한다.

  ```python
  from enum import Enum, auto
  
  class Color(Enum):
  
      RED = auto()
      BLUE = auto()
      GREEN = auto()
  
  print(list(Color))
  # [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
      
  class Color(Enum):
      def _generate_next_value_(name, start, count, last_values):
          return name
  
      RED = auto()
      BLUE = auto()
      GREEN = auto()
  
  print(list(Color))
  # [<Color.RED: 'RED'>, <Color.BLUE: 'BLUE'>, <Color.GREEN: 'GREEN'>]
  ```

<br>

---

<br>
