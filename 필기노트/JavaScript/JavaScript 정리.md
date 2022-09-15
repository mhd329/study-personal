# JavaScript

<br>

## 목차

<br>

[1. 브라우저와 JavaScript](#1-브라우저와-JavaScript)

[2. 파편화와 표준화](#2-파편화와-표준화)

[3. 브라우저에서 할 수 있는 일들](#3-브라우저에서-할-수-있는-일들)

[4. DOM 선택과 조작](#4-DOM-선택과-조작)

<br>

## 1. 브라우저와 JavaScript

<br>

- URL 로 웹을 탐색하여 서버와 통신
- HTML 문서나 파일을 출력해주는 GUI 기반의 소프트웨어
- 브라우저를 통해 인터넷에 있는 여러 가지들을 볼 수 있다.
- JavaScript 를 통해 브라우저 화면을 동적으로 만들 수 있다.
- 브라우저를 조작할 수 있는 유일한 언어이기 때문에 전 세계에서 언어 사용자의 수가 가장 많다.

<br>

[위로 가기](#목차)

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

[위로 가기](#목차)

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

[위로 가기](#목차)

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
