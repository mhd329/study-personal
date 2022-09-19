# JavaScript 정리

<br>

## 목차

<br>

[1. JavaScript 란 무엇일까?](#1-JavaScript-란-무엇일까?)

[2. JavaScript 로 할 수 있는 일들](#2-JavaScript-로-할-수-있는-일들)

[3. 기본적인 문법과 자료형](#3-기본적인-문법과-자료형)

> [3-1. 변수와 선언](#3-1-변수와-선언)
>
> [3-2. 데이터 구조 및 형](#3-2-데이터-구조-및-형)
>
> [3-3. 배열](#3-3-배열)
>
> [3-4. 불리언 리터럴](#3-4-불리언-리터럴)

[4. 제어](#4-제어)

>[4-1. 조건문](#4-1-조건문)
>
>[4-2. 스위치문](#4-2-스위치문)
>
>[4-3. 예외처리](#4-3-예외처리)

[5. 반복](#5-반복)

[6. 함수](#6-함수)

>[6-1. 함수 만들기](#6-1-함수-만들기)
>
>[6-2. 함수 호출](#6-2-함수-호출)
>
>[6-3. 클로저](#6-3-클로저)

[7. 인수](#7-인수)

[8. 매개변수](#8-매개변수)

[9. 연산자](#9-연산자)

<br>

### 1. JavaScript 란 무엇일까?

<br>

- 웹 페이지를 구성하는 것들
  - HTML : 웹 페이지의 뼈대
  - CSS : 살을 붙이고 꾸미기
  - Javascript : 그리고 움직임을 준다.
- Javascript 는 컨텐츠들에 동적 요소를 주어 페이지를 방문하는 사용자들에게 더 나은 경험을 제공할 수 있게 해주는 언어이다.

<br>

```javascript
const para = document.querySelector('p');

para.addEventListener('click', updateName);

function updateName() {
  const name = prompt('Enter a new name');
  para.textContent = `Player 1: ${name}`;
}
```

- HTML, CSS 로 꾸미는 과정은 생략하고 Javascript 로 변수 선언과 문자열 조작 및 함수를 통해 p 태그에 대해 동적인 요소를 주었다.

<br>

[위로 가기](#목차)

<br>

### 2. JavaScript 로 할 수 있는 일들

<br>

- API 를 이용
  - 브라우저 APIs
    - 브라우저에 내장된 API
    - 현재 컴퓨터 환경에 관한 데이터를 제공
    - 그 외 여러가지 작업을 수행
      - DOM API 로 HTML/CSS 를 동적으로 조작
      - 지오로케이션 API 로 지리정보 가져오기
      - 캔버스와 웹GL API 로 애니메이션을 적용한 2D 3D 그래픽 만들기
      - 오디오와 비디오 API 로 멀티미디어 조작
  - 서드파티 APIs
    - 브라우저에 탑재되지 않은 API
    - 어딘가에서 직접 코드와 정보를 찾아야 한다.
      - 트위터 API
      - 구글지도 API 등
- 클라이언트 사이드, 서버 사이드 둘 다 사용 가능
- HTML 파일 내부에서 `<script>` 요소 안에 JavaScript 를 넣거나,
- script.js 와 같이 .js 파일로 사용할 수 있다.

<br>

[위로 가기](#목차)

<br>

## 3. 기본적인 문법과 자료형

<br>

- 대소문자 구분
- 유니코드 문자셋을 이용
- Java, C, C++ 로부터 차용하고 있으며 Awk, Perl, Python의 영향도 받았다.

```javascript
// 뒤에 세미콜론은 쓰지 않아도 작동한다.

var ab = "cd";
var 갑을 = "병정";
var Früh = "foobar";

// 한 줄 주석

/* 이것은 여러 줄을 주석 처리 할 때,
쓰이는 주석 처리법이다. */

/* 그러나 */ 주석을 중첩해서 사용할 수 없다. */ SyntaxError */
```

<br>

[위로 가기](#목차)

<br>

### 3-1. 변수와 선언

<br>

- `var` 변수를 선언하거나 값을 초기화
- `let` 블록 스코프 지역 변수를 선언하거나 값을 초기화
- `const` 블록 스코프 읽기 전용 상수를 선언
  - 선언 후 변경할 수 없다.
  - 임의의 값으로 초기화해야 한다.
- 변수명은 문자, 언더바, 달러기호로 시작할 수 있지만 숫자로 시작할 수 없다.
- 선언할 때 `var` , `let` 을 통해 값을 넣지 않고 변수만 선언할 수 있다.
- 변수만 선언된 경우 undefined 값을 가진다.
  - undefined 는 다음과 같다.
    - false
    - NaN
  - Null 값은 다음과 같다.
    - false
    - 0

<br>

- 변수의 스코프

  ```javascript
  if (true) {
    var x = 5;
  }
  console.log(x); // 5
  
  if (true) {
    let y = 5;
  }
  console.log(y); // ReferenceError: y is not defined
  ```

- 변수 호이스팅

  ```javascript
  /*
  Example 1
  */
  
  console.log(x === undefined); // true
  var x = 3;
  
  
  /*
  Example 2
  */
  
  // undefined 값을 반환함.
  var myvar = "my value";
  
  (function() {
    console.log(myvar); // undefined
    var myvar = "local value";
  })();
  
  
  
  
  
  /*
  Example 1
  */
  var x;
  console.log(x === undefined); // true
  x = 3;
  
  /*
  Example 2
  */
  var myvar = 'my value';
  
  (function() {
    var myvar;
    console.log(myvar); // undefined
    myvar = 'local value';
  })();
  
  
  
  console.log(x); // ReferenceError
  let x = 3;
  ```


- 함수 호이스팅

  ```javascript
  /* 함수 선언 */
  
  foo(); // "bar"
  
  function foo() {
    console.log('bar');
  }
  
  /* 함수 표현식 */
  
  baz(); // TypeError: baz is not a function
  
  var baz = function() {
    console.log('bar2');
  };
  ```

- 상수 선언

  ```javascript
  // 오류가 발생합니다
  function f() {};
  const f = 5;
  
  // 역시 오류가 발생합니다
  function f() {
    const g = 5;
    var g;
  
    //statements
  }
  
  const MY_OBJECT = {'key': 'value'};
  MY_OBJECT.key = 'otherValue';
  // 오류 없음
  
  const MY_ARRAY = ['HTML','CSS'];
  MY_ARRAY.push('JAVASCRIPT');
  console.log(MY_ARRAY); //logs ['HTML','CSS','JAVASCRIPT'];
  // 오류 없음
  ```

<br>

[위로 가기](#목차)

<br>

### 3-2. 데이터 구조 및 형

<br>

- 원시 데이터 형

  1. Boolean
  2. null
     - `null`은 `Null`, `NULL` 혹은 다른 변형과도 다르다.
  3. undefined
     - 값이 정의되어 있지 않은 최상위 속성
  4. Number
     - 정수, 실수
  5. BigInt
     - 임의 정밀도의 정수
  6. String
  7. Symbol
     - (ES6+) 인스턴스가 고유하고 불변인 데이터 형.

- Object

- 데이터 형이 스크립트 실행 도중 필요에 의해 자동으로 변환된다.

- 숫자와 문자 사이에 덧셈 연산자를 사용할 경우 숫자가 자동으로 문자열로 바뀐다.

  ```javascript
  x = 'The answer is ' + 42 // "The answer is 42"
  y = 42 + ' is the answer' // "42 is the answer"
  ```

- 문자열을 숫자로 변환하는 메서드

  - `parseInt()`

    - 정수만 반환

    - ```javascript
      parseInt('101', 2) // 5
      ```

  - ``parseFloat()`

<br>

[위로 가기](#목차)

<br>

### 3-3. 배열

<br>

- 파이썬의 리스트와 비슷하다.

- 추가 쉼표를 주면 지정되지 않은 요소를 undefined 로 정한다.

  ```javascript
  let fish = ['Lion', ,'Angel']; // fish[1] 은 undefined
  ```

- 배열의 마지막이 쉼표로 끝난다면 무시한다.

- 구버전에서는 오류가 날 수 있기 때문에 지우는 것이 좋다.

  ```javascript
  var myList = ['home', ,'school', ,];
  
  /*
  배열의 길이는 4
  구버전에서는 오류가 날 수 있다.
  마지막 쉼표가 지워지면 길이는 3이 되고
  'school' 뒤의 쉼표는 무시된다.
  */
  ```

<br>

[위로 가기](#목차)

<br>

### 3-4. 불리언 리터럴

<br>

- 불리언 형은 `true `와 `false `의 리터럴 값을 가진다.
- 서로 다름
  - 원시 불리언 값 `true` 및 `false`
  - `Boolean` 객체의 true 및 false 값

<br>

[위로 가기](#목차)

<br>

## 4. 제어

<br>

- 블록문은 제어문의 기본 단위이다.

- 명령문들을 그룹으로 묶은 것

  ```javascript
  {
    statement_1;
    statement_2;
    ⋮
    statement_n;
  }
  ```

- `if, for, while` 문들 과 같이 사용함

<br>

[위로 가기](#목차)

<br>

### 4-1. 조건문

<br>

- if, else 등 기본적인 조건문

  ```javascript
  if (condition) {
    statement_1;
  } else {
    statement_2;
  }
  
  
  
  if (condition_1) {
    statement_1;
  } else if (condition_2) {
    statement_2;
  } else if (condition_n) {
    statement_n;
  } else {
    statement_last;
  }
  ```

- 조건문을 중첩해서 사용할 때 블록문을 함께 사용하는 것이 좋다.

  ```javascript
  if (condition) {
    statement_1_runs_if_condition_is_true;
    statement_2_runs_if_condition_is_true;
  } else {
    statement_3_runs_if_condition_is_false;
    statement_4_runs_if_condition_is_false;
  }
  ```

- false 의 종류
  - false
  - undefined
  - null
  - 0
  - NaN
  - ( 공백도 없는 ) 빈 문자열

<br>

[위로 가기](#목차)

<br>

### 4-2. 스위치문

<br>

- case 를 사용하여 각 경우마다 실행되는 명령이 달라진다.

  ```javascript
  switch (expression) {
    case label_1:
      statements_1;
      break;
    case label_2:
      statements_2;
      break;
      …
    default:
      statements_default;
  }
  
  
  
  switch (fruittype) {
    case '오렌지':
      console.log('오렌지는 파운드 당 $0.59입니다.');
      break;
    case '사과':
      console.log('사과는 파운드 당 $0.32입니다.');
      break;
    case '바나나':
      console.log('바나나는 파운드 당 $0.48입니다.');
      break;
    case '체리':
      console.log('체리는 파운드 당 $3.00입니다.');
      break;
    case '망고':
      console.log('망고는 파운드 당 $0.56입니다.');
      break;
    case '파파야':
      console.log('망고와 파파야는 파운드 당 $2.79입니다.');
      break;
    default:
      console.log(`죄송합니다. ${fruitType}은 품절입니다.`);
  }
  console.log('더 필요한게 있으신가요?');

<br>

[위로 가기](#목차)

<br>

### 4-3. 예외처리

<br>

- throw 를 통해 예외를 던진다.

  ```javascript
  /* throw expression; */
  
  throw 'Error2'; // String
  throw 42; // Number
  throw true; // Boolean
  throw {
    toString: function () {
      return '저는 객체예요';
    },
  };
  ```

  - 숫자나 문자열을 예외로 던질 수 있다.

  - 그러나 사전에 정의된 유형을 쓰는 것이 효과적이다.

- 던진 예외는 try, catch 로 처리할 수 있다.

-  finally 블록에 있는 명령은 try, catch 가 끝난 후 항상 실행된다.

  - 예외의 발생 여부를 따지지 않는다.

- 예외처리 예시

  ```javascript
  function getMonthName(mo) {
    mo = mo - 1; // 배열 인덱스에 맞춰 월 조절 (1 = Jan, 12 = Dec)
    let months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    if (months[mo]) {
      return months[mo];
    } else {
      throw 'InvalidMonthNo'; // 여기서 throw 키워드 사용
    }
  }
  
  try {
    // 시도할 명령문
    monthName = getMonthName(myMonth); // 예외가 발생할 수 있는 함수
  } catch (e) {
    monthName = 'unknown';
    logMyErrors(e); // 오류 처리기에 예외 객체 전달
  }
  
  
  
  openMyFile();
  try {
    writeMyFile(theData); // 오류가 발생할 수 있는 코드
  } catch (e) {
    handleError(e); // 오류가 발생하면 처리함
  } finally {
    closeMyFile(); // 항상 리소스 해제
  }
  
  
  
  function f() {
    try {
      console.log(0);
      throw 'bogus';
    } catch (e) {
      console.log(1);
      return true; // finally 블록의 실행이 끝날 때까지 중단됨
      console.log(2); // 접근 불가
    } finally {
      console.log(3);
      return false; // 앞선 return보다 우선함
      console.log(4); // 접근 불가
    }
    // return false가 실행됨
    console.log(5); // 접근 불가
  }
  console.log(f()); // 0, 1, 3, false
  ```

<br>

[위로 가기](#목차)

<br>

## 5. 반복

<br>

- C의 반복문과 비슷하다.

  - for 문

  - ```javascript
    for ([초기문]; [조건문]; [증감문])
    	문장
    ```

  - do while 문

  - ```javascript
    do
    	문장
    while (조건문);
    ```

  - while 문

  - ```javascript
    while (조건문)
    	문장
    ```
  
  - for in 문
  
  - ```javascript
    for (variable in object) {
    	statements
    }
    ```
  
  - for of 문
  
  - ```javascript
    for (variable of object) {
    	statement
    }
    ```
  
    - for in, for of 차이
  
    - ```javascript
      let arr = [3, 5, 7];
      arr.foo = "hello";
      
      for (let i in arr) {
         console.log(i); // logs "0", "1", "2", "foo"
      }
      
      for (let i of arr) {
         console.log(i); // logs "3", "5", "7"
      }
      ```
    
    - for in 에서는 인덱스 내부 요소의 내용을 출력하는 것이 아니고 인덱스 내부 각 개체의 프로퍼티 키를 가져온다.
    
    - 즉 `arr[0]` 의 값은 3 이지만 인덱스 번호는 0 이므로 처음으로 0 이 찍힌다.


- 종료 시 break 를 쓴다.

  - ```javascript
    break;
    break 레이블;
    ```

- while, do-while, for, 레이블 문을 다시 시작하는 경우 continue 를 쓴다.

  - ```javascript
    continue;
    continue 레이블;
    ```

<br>

[위로 가기](#목차)

<br>

## 6. 함수

<br>

- JavaScript 명령을 수행하는 문장의 집합

- 함수 정의의 기본적인 형태

  ```javascript
  function square(number) {
    return number * number;
  }
  ```

- 함수 표현식

  - 익명함수 선언

  ```javascript
  var square = function(number) { return number * number };
  var x = square(4) // x 의 값은 16 입니다.
  
  // 이름을 지어줄 수도 있다.
  
  var factorial = function fac(n) { return n<2 ? 1 : n*fac(n-1) };
  console.log(factorial(3));
  ```

  - 함수 표현식은 함수를 다른 함수의 매개변수로 전달할 때 좋다.
    - map 같은 곳에서 쓰일 수 있다. 

- 함수를 어떤 조건이 만족될 때에만 정의되게끔 만들 수도 있다.

  ```javascript
  var myFunc;
  if (num == 0){
    myFunc = function(theObject) {
      theObject.make = "Toyota"
    }
  }
  ```

<br>

[위로 가기](#목차)

<br>

### 6-1. 함수 만들기

<br>

```javascript
function 함수 이름 ( 받을 인자 ) {
    실행시킬 명령
}
```

<br>

[위로 가기](#목차)

<br>

### 6-2. 함수 호출

<br>

- 함수 호출은 파이썬과 비슷하게 호출한다.

- 함수 호출은 호이스팅 될 수 있다.

  - 호출시 이름이 겹치지 않게 주의

  ```javascript
  console.log(square);   // square는 초기값으로 undefined를 가지고 호이스트된다.
  console.log(square(5));  // TypeError: square는 함수가 아니다.
  square = function (n) {
    return n * n;
  }
  ```

- 재귀가 가능하다.

- 함수 내에 다른 함수를 끼워넣을 수 있다.

- 중첩된 내부 함수가 반환될 때 외부 함수의 인수가 보존된다.

- 이름이 충돌될 수 있다.

  ```javascript
  function outside() {
    var x = 10;
    function inside(x) {
      return x;
    }
    return inside;
  }
  result = outside()(20); // returns 20 instead of 10
  
  // 내부 함수가 받은 20 이 외부 함수의 x 보다 우선순위가 높기 때문에 20 이 반환된다.
  ```

<br>

[위로 가기](#목차)

<br>

### 6-3. 클로저

<br>

- JavaScript 는 함수의 중첩을 허용한다.

- 내부 함수는 외부 함수의 모든 것에 접근할 수 있지만 그 반대의 경우는 불가능하다.

  ```javascript
  var pet = function(name) {   // 외부 함수는 'name'이라 불리는 변수를 정의합니다.
    var getName = function() {
      return name;             // 내부 함수는 외부 함수의 'name' 변수에 접근합니다.
    }
    return getName;            // 내부 함수를 리턴함으로써, 외부 범위에 노출됩니다.
  },
  myPet = pet("Vivie");
  
  myPet();                     // "Vivie"로 리턴합니다.
  ```

- 내부와 외부의 어떤 변수가 같은 변수명을 가지게 되면 외부 변수에 접근할 수 없게 된다.

  ```javascript
  var createPet = function(name) {  // 외부 함수가 "name" 이라는 변수를 정의하였다
    return {
      setName: function(name) {    // 내부 함수 또한 "name" 이라는 변수를 정의하였다
        name = name;               // ??? 어떻게 우리는 외부 함수에 정의된 "name"에 접근할까???
      }
    }
  }
  ```

<br>

[위로 가기](#목차)

<br>

## 7. 인수

<br>

- 함수의 인수는 배열과 비슷한 객체로 처리된다.

- 함수 내에서는 인수를 `arguments[i]` 처럼 다룰 수 있다.

  - 전체 인수의 개수는 `arguments.length` 로 얻을 수 있다.

  ```javascript
  function myConcat(separator) {
     var result = ""; // 리스트를 초기화한다
     var i;
     // arguments를 이용하여 반복한다
     for (i = 1; i < arguments.length; i++) {
        result += arguments[i] + separator;
     }
     return result;
  }
  
  // returns "red, orange, blue, "
  myConcat(", ", "red", "orange", "blue");
  
  // returns "elephant; giraffe; lion; cheetah; "
  myConcat("; ", "elephant", "giraffe", "lion", "cheetah");
  
  // returns "sage. basil. oregano. pepper. parsley. "
  myConcat(". ", "sage", "basil", "oregano", "pepper", "parsley");
  ```

<br>

[위로 가기](#목차)

<br>

## 8. 매개변수

<br>

- 기본적으로 `undefined` 가 설정된다.

- 디폴트값을 주는 경우 함수 호출시 필요한 수 만큼 값이 전달되지 않으면 기본값이 대신한다.

  - 파이썬과 비슷한 방식이다.

- 나머지 매개변수 구문

  - 불확실한 개수의 인수를 나타낼 수 있다.

  - 화살표 함수를 사용하여 나타낼 수 있다.

    ```javascript
    function multiply(multiplier, ...theArgs) {
      return theArgs.map(x => multiplier * x);
    }
    
    var arr = multiply(2, 1, 2, 3);
    console.log(arr); // [2, 4, 6]
    ```

- 화살표 함수

  - 언제나 익명인 함수이다.
  - 사전적으로 this 값을 묶는다.
    - this 는 파이썬의 self 와 같다.

  ```javascript
  var a = [
    "Hydrogen",
    "Helium",
    "Lithium",
    "Beryllium"
  ];
  
  var a2 = a.map(function(s){ return s.length });
  
  console.log(a2); // logs [8, 6, 7, 9]
  
  var a3 = a.map( s => s.length );
  
  console.log(a3); // logs [8, 6, 7, 9]
  ```

<br>

[위로 가기](#목차)

<br>

## 9. 연산자

<br>

- 여러 종류의 [연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators)가 있다.
  - 할당 연산자
  - 비교 연산자
  - 산술 연산자
  - 비트 연산자
  - 논리 연산자
  - 문자열 연산자
  - 조건 (삼항) 연산자
  - 쉼표 연산자
  - 단항 연산자
  - 관계 연산자

<br>

[위로 가기](#목차)

<br>

## 10. EventTarget

<br>

- `EventTarget.addEventListener()`
  - 이벤트 수신기
  - 지정한 유형의 이벤트가 실행될 때마다 수신기를 통해 호출할 함수를 설정한다.
  - `addEventListener(type, listener, options);`
    - `type` 이벤트의 종류
    - `listener` 지정한 이벤트를 받을 객체
      - 주로 콜백 함수의 형태로 쓰임
    - `option` 이벤트 수신기의 세부적인 특징 설정
      - 옵션값이다.
    - 반환되는 값은 `undefined`

<br>

- 브라우저 버전에 따른 `option` 지원 여부 알아보기
  - 구형 브라우저에서는 세 번째 인자로 주어지는 `option` 에 오직 불리언 값만 기대하고 있는 경우가 있다.
  - 그 여부를 감지하여 처리할 수 있는 코드를 작성할 필요가 있다.
  - 직접 알아내는 대신 Modernizr, Detect It 등을 이용하여 알아낼 수도 있다.

<br>

[위로 가기](#목차)

<br>
