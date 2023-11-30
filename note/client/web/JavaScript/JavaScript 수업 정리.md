# JavaScript

<br>

## 목차

<br>

[1. 브라우저와 JavaScript](#1-브라우저와-JavaScript)

[2. 파편화와 표준화](#2-파편화와-표준화)

[3. 브라우저에서 할 수 있는 일들](#3-브라우저에서-할-수-있는-일들)

[4. DOM 선택과 조작](#4-DOM-선택과-조작)

[5. 변수와 식별자](#5-변수와-식별자)

[6. 데이터 타입](#6-데이터-타입)

[7. 연산자](#7-연산자)

[8. 조건문](#8-조건문)

[9. 반복문](#9-반복문)

[10. 함수](#10-함수)

[11. 문자열](#11-문자열)

[12. 배열](#12-배열)

[13. 객체](#13-객체)

[14. 이벤트](#14-이벤트)

<br>

## 1. 브라우저와 JavaScript

<br>

- URL 로 웹을 탐색하여 서버와 통신
- HTML 문서나 파일을 출력해주는 GUI 기반의 소프트웨어
- 브라우저를 통해 인터넷에 있는 여러 가지들을 볼 수 있다.
- JavaScript 를 통해 브라우저 화면을 동적으로 만들 수 있다.
- 브라우저를 조작할 수 있는 유일한 언어이기 때문에 전 세계에서 언어 사용자의 수가 가장 많다.

<br>

## 2. 파편화와 표준화

<br>

- 세상에는 다양한 브라우저들이 있다.
- 각 브라우저마다 자체적인 JavaScript 언어를 사용하였다.
- 때문에 브라우저간 호환이 안되서 많은 문제가 발생하였다.
  - 웹 표준의 필요성이 제기되었다.
  - ECMAScript 1 줄여서 ES1 의 탄생
- 현재는 표준의 대부분이 ES6+ 로 넘어왔다.
- ES6 이후 순수 자바스크립트 활용이 늘어남

<br>

## 3. 브라우저에서 할 수 있는 일들

<br>

- DOM 조작
- BOM 조작
- JS Core

<br>

- DOM
  - 문서 조작용 프로그래밍 인터페이스
  - 문서를 구조화하고 그 구성 요소를 객체로 취급
    - window
    - document
    - navigator, location, history, screen
  - 해석과정을 거쳐서 DOM Tree 로 만든다.

<br>

- BOM
  - JavaScript 가 브라우저와 소통하기 위한 모델
  - 브라우저 요소들을 추상화해서 제어할 수 있게 해주는 수단
- JS Core
  - 프로그래밍 언어

<br>

## 4. DOM 선택과 조작

<br>

- ```javascript
  document.querySelector('선택자')
  ```

  - 선택자와 일치하는 것 하나를 선택
  - 첫 번째 element 객체를 반환하고 없다면 null

- ```javascript
  document.querySelectorAll('선택자')
  ```

  - 선택자와 일치하는 여러개를 선택
  - NodeList 를 반환

- ```javascript
  getElementById(id)
  getElementsByTagName(name)
  getElementsByClassName(names)
  ```

- 단일 element 반환 타입

  - `qureySelector()`

- NodeList 반환 타입

  - `querySelectorAll()`

- HTMLCollection, NodeList

  - 배열처럼 index 제공
  - HTMLCollection
    - name, id, index 속성으로 각 항목에 접근 가능
  - NodeList
    - index 로만 가능
    - forEach 메서드 등 다양한 메서드 사용 가능

- Collection

  - Live Collection
    - 문서가 바뀔 때 실시간으로 변경
    - HTMLCollection, NodeList
  - Static Collection
    - 문서가 바뀌어도 collection 은 변경 없음
    - `querySelectorAll() ` 로 반환된 NodeList 만 static collection 이다.

<br>

- `document.createElement()`
  - 작성한 태그 이름의 HTML 요소가 반환된다.
- `Element.setAttribute(name, value)`
  - 지정된 요소의 값을 설정
- `Element.getAttribute(attributeName)`
  - 지정값을 문자열로 반환

<br>

[위로 가기](#목차)

<br>

## 5. 변수와 식별자

<br>

- 식별자 == 변수를 구분할 수 있는 변수명
- 문자, 달러, 언더바로 시작한다.
- 대소문자 구분
  - 클래스 이름 외에는 모두 소문자로 시작
- 예약어로 할 수 없다.
- 선언
  - 변수를 생성하는 행위
  - 할당
    - 그 변수에 값을 저장
- 초기화
  - 선언과 할당을 동시에 함
- `const` 는 선언 및 초기값 할당 후 재할당 할 수 없다.
- `let` 과 `const` 는 초기화 후 재선언 할 수 없다.
  - 블록 스코프
    - 중괄호 내부를 가리킨다.
    - 블록 스코프를 가지는 변수는 그 블록의 바깥에서 접근할 수 없다.
- `var` 는 재선언 및 재할당 모두 가능하다.
  - 호이스팅 특성으로 인해 예외가 발생할 수 있다.
    - ES6 이후부터는 var 대신 let 이나 const 사용이 권장된다.
  - 함수 스코프
    - 함수의 중괄호 내부를 가리킴
    - 함수 스코프를 가지는 변수는 함수의 바깥에서 접근할 수 없다.

<br>

[위로 가기](#목차)

<br>

## 6. 데이터 타입

<br>

- 모든 값은 특정한 데이터 타입을 가진다.
- 크게 원시 타입과 참조 타입으로 나뉘어진다.
- 원시 타입
  - 객체가 아닌 기본타입
  - 변수에 해당 타입의 값이 담김
  - 다른 변수에 복사할 때 실제 값이 복사된다.
- 참조 타입
  - 객체 타입
  - 변수에 해당 객체의 참조값이 담김
  - 다른 변수에 복사할 때 참조값이 복사됨
- 숫자
  - 정수, 실수 구분없는 하나의 숫자 타입
  - 부동소수점 형식을 따름
- 문자열
  - 텍스트 데이터
  - 16비트 유니코드 문자의 집합
- `undifined`
  - 변수 선언 이후 값을 할당하지 않을 시 `undifined` 가 할당된다.
- `null`
  - 의도적으로 변수에 값이 없다는 것을 표현
  - `null` 타입은 원시 타입 이지만 `typeof` 연산자로는 객체라고 나온다.
- `Boolean`
  - true, false
  - 조건문, 반복문에서 자주 사용

<br>

[위로 가기](#목차)

<br>

## 7. 연산자

<br>

- 할당
  - 값을 할당해줌
- 비교
  - 두 개를 비교 후 boolean 값을 반환
  - 문자열 비교는 유니코드 값을 사용
    - A < Z
    - A < a
- 동등 비교
  - ==
  - 암묵적 타입 변환을 통해 값을 일치시킨다.
  - 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
  - [특별한 경우](https://google.github.io/styleguide/jsguide.html#features-equality-checks-exceptions)를 제외하고는 사용하지 않음
- 일치 비교
  - ===
  - 엄격한 비교가 이루어진다.
  - 타입 변환 없음
- 논리
  - and, or, not
- 삼항
  - 세 개를 비교
  - 왼쪽의 조건식이 참이면 콜론 앞, 그렇지 않으면 콜론 뒤
  - 변수에 할당할 수 있다.
  - 한줄 표기가 권장된다.

<br>

[위로 가기](#목차)

<br>

## 8. 조건문

<br>

- if 와 switch
- if 문
  - 조건은 소괄호 안에 작성
  - 실행할 코드는 중괄호 안에 작성
    - if
    - else if
    - else
- switch 문
  - 표현식의 결과값을 이용한 조건문
  - 표현식의 결과값과 case 문의 오른쪽을 비교
    - case
    - break
    - default
  - break 와 default 는 선택적 이용 가능
  - 다만 break 가 없으면 어떤 조건이 맞아도 멈추지 않고 끝까지 실행된다.

<br>

[위로 가기](#목차)

<br>

## 9. 반복문

<br>

- while
- for
- for in
  - 객체의 속성 순회시 사용
  - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없다.
- for of
  - 반복가능한 객체를 순회하며 값을 꺼낼 때 사용

<br>

[위로 가기](#목차)

<br>

## 10. 함수

<br>

- 참조 타입중 하나
- 함수 선언식과 함수 표현식이 있다.
- JavaScript 의 함수는 일급 객체에 해당한다. 즉,
  - ( 함수를 ) 변수에 할당 가능
  - 함수의 매개변수로 전달 가능
  - 함수의 반환값으로 사용 가능

<br>

- 세 가지 부분으로 구성
  - 이름
  - 매개변수
  - 몸통
- 함수 표현식
  - 함수를 표현식 내에서 정의하는 방식
  - 익명으로 쓸 수 있음
    - 함수 표현식에서만 가능

<br>

- 기본인자를 설정할 수 있다.

<br>

- 인자의 개수가 다를 경우 과부족한 만큼 `undifined` 를 준다.

<br>

- rest parameter 를 사용할 경우 정해지지 않은 수의 매개변수를 배열로 받을 수 있다.
  - 파이썬의 `*args` 와 같다.

<br>

- spread operator 를 사용하면 배열 인자를 전개할 수 있다.

<br>

- 호이스팅
  - 함수 선언식으로 사용하면 호이스팅 가능
  - 함수 표현식으로 사용하면 변수로 평가되어 변수의 스코프 규칙을 따르기 때문에 에러가 난다.

<br>

---

##### 화살표 함수

- 함수를 비교적 간단하게 정의할 수 있게 해주는 문법
- function 키워드 생략 가능
- 매개변수가 하나라면 소괄호 생략 가능
- 몸통이 표현식 하나라면 중괄호와 return 생략 가능

---

<br>

[위로 가기](#목차)

<br>

## 11. 문자열

<br>

- 주요 메서드
  - `string.includes("어떤 값")`
    - 참 또는 거짓 반환
  - `string.split("어떤 값")`
  - `string.replace("어떤 값")`
  - `string.replaceAll("어떤 값")`
  - `string.trim()`
    - 파이썬의 `strip()`
    - `string.trimStart(), string.trimEnd()`

<br>

[위로 가기](#목차)

<br>

## 12. 배열

<br>

- 키와 속성들을 담고 있는 참조 타입의 객체

- 파이썬의 리스트와 비슷한 특징을 가진다.

- 원소를 뒤에서부터 세려면 `array.length – 1` 로 뒤에서부터 셀 수 있다.

- 주요 메서드들

  - `array.reverse()` == `sort(reverse = True)`

  - `array.push()` == `append`

  - `array.pop()`

  - `array.unshift()` == `insert(0, 추가할 값)`

  - `array.shift()` == `pop(0)`

  - `array.includes(어떤 값)` == `if 어떤 값 in list`

    - 참 또는 거짓 반환

  - `array.indexOf(어떤 값)` == `find(어떤 값)`

    - `find(어떤 값)` 처럼 찾는 대상이 없는 경우 -1 을 반환한다.

  - `array.join(구분자)` == `''.join(list)`

    - 생략하는 경우 쉼표를 기본 값으로 사용한다.

  - spread operator 를 사용하는 경우 배열 내부에서 배열의 전개가 가능하다.

    - 얕은 복사에 활용할 수 있다.

    ```javascript
    const array = [1, 2, 3]
    const newArray = [0, ...array, 4]
    console.log(newArray) // [0, 1, 2, 3, 4]
    ```

<br>

- 심화 메서드들
  - `array.forEach((element, index, array) => { 실행할 코드 })`
    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
      - element
        - 배열의 요소
      - index
        - 배열 요소의 인덱스
      - array
        - 배열 자체
    - 반환값이 없는 메서드이다.
  - `array.map((element, index, array) => { 실행할 코드 })`
    - 콜백 함수의 반환값을 요소로 하는 새로운 배열 반환
    - 기존의 배열 전체를 다른 형태로 바꿀 때 유용하다.
  - `array.filter((element, index, array) => { 실행할 코드 })`
    - 참인 요소들만 모아서 새로 만듦
  - `array.reduce((acc, element, index, array) => { 실행할 코드 }, initialValue)`
    - 반환값들을 하나의 값에 누적 후 반환
      - acc
        - 이전의 콜백 반환값이 누적되는 변수
      - initialValue
        - 옵션이다.
        - 최초 콜백 호출시 acc 에 할당되는 값
        - default 값은 배열의 첫 번째 값
    - 빈 배열의 경우 initialValue 을 주지 않으면 에러가 난다.
  - `array.find((element, index, array) => { 실행할 코드 })`
    - 반환값이 참이면 그 조건을 만족하는 첫 번째 요소를 반환
    - 없다면 undefined 를 반환한다.
  - `array.some((element, index, array) => { 실행할 코드 })`
    - 요소 중 하나라도 주어진 함수를 통과하면 참을 반환, 그렇지 않으면 거짓 반환
    - 빈 배열은 항상 거짓 반환
  - `array.every((element, index, array) => { 실행할 코드 })`
    - 모든 요소가 통과해야 참, 그렇지 않다면 거짓
    - 빈 배열은 항상 참

<br>

[위로 가기](#목차)

<br>

## 13. 객체

<br>

- 속성의 집합
- 중괄호 내부에 키와 값의 쌍으로 표현된다.
  - 키는 문자열 타입만 가능하다.
    - 키 이름에 띄어쓰기가 있다면 따옴표로 묶어서 표현
  - 값은 모든 타입이 가능하다.
- `객체.키` 혹은 `객체.['키']` 로 접근이 가능하다.
  - 키 이름에 띄어쓰기가 있다면 대괄호 접근만 가능하다.
  - `객체.['이것은 키']`
- 메서드는 객체의 속성이 참조하는 함수
- `객체.메서드명()` 으로 호출 가능
- 메서드 내부에서는 this 키워드가 객체를 의미한다.
  - 파이썬의 self 와 같다.

---

##### JSON

- 키와 값의 쌍으로 데이터를 표기하는 언어 독립적 표준 포맷
- JavaScript 의 객체와 비슷하게 생겼다.
  - 실제로는 문자열 타입이다.
  - JavaScript 의 객체로 조작하기 위해서는 구문 분석이 필수이다.
  - JSON 조작을 위한 두 가지 내장 메서드를 제공하고 있다.
    - `JSON.parse()`
      - JSON 에서 자바스크립트 객체로 변환
    - `JSON.stringify()`
      - 자바스크립트 객체에서 JSON 으로 변환

<br>

[위로 가기](#목차)

<br>

## 14. 이벤트

<br>

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
  - 마우스 클릭, 키보드 키 누르기 등의 사용자 행동으로 인해 발생
  - 특정 메서드를 호출하는 식으로 의도적 설계도 가능
- 이벤트 핸들러
  - `addEventListener()`
    - 이벤트를 듣는 객체
    - `target.addEventListener(type, listener, options)`
      - `type` 이벤트의 유형 ( click, input 등, 대소문자 구분 문자열 )
      - `listener` 이벤트가 발생했다는 신호를 받을 객체
        - EventListener 인터페이스 혹은 JS function 객체 ( 콜백함수 ) 여야 함
- 이벤트 취소
  - `event.preventDefault()`
    - 현재 이벤트의 기본 동작을 중단
    - HTML 요소의 기본 동작을 작동하지 않게 막음
      - copy 같은 이벤트가 발생했을 때 복사를 막음
      - a 태그 링크 이동을 막음 등
    - 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소
      - 취소할 수 없는 이벤트도 있다.
      - 이벤트의 취소 가능 여부는 `event.cancelable` 을 사용해 확인할 수 있음

<br>

[위로 가기](#목차)

<br>
