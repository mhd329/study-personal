# HTML

<br>

## 목차

<br>

[1. 웹 사이트의 구성 요소](#1-웹-사이트의-구성-요소)

[2. 웹 사이트와 브라우저](#2-웹-사이트와-브라우저)

[3. 개발 환경 설정](#3-개발-환경-설정)

[4. HTML 기초](#4-HTML-기초)

> [4-1. HTML 기본 구조](#4-1-HTML-기본-구조)
>
> >[4-1-1. html](#4-1-1-html)
> >
> >[4-1-2. head](#4-1-2-head)
> >
> >[4-1-3. body](#4-1-3-body)
>
> [4-2. HTML 태그](#4-2-HTML-태그)
>
> >[4-2-1. 시맨틱 태그](#4-2-1-시맨틱-태그)
> >
> >[4-2-2. Table](#4-2-2-Table)
> >
> >[4-2-3. form](#4-2-3-form)
> >
> >[4-2-4. input](#4-2-4-input)

[5. CSS](#5-CSS)

> [5-1. CSS 기본 스타일](#5-1-CSS-기본-스타일)
>
> > [5-1-1. CSS 선택자](#5-1-1-CSS-선택자)
> >
> > [5-1-2. CSS BOX model](#5-1-2-CSS-BOX-model)
> >
> > [5-1-3. CSS Display](#5-1-3-CSS-Display)
> >
> > [5-1-4. CSS Position](#5-1-4-CSS-Position)
>
> [5-2. CSS Layout](#5-2-CSS-Layout)
>
> [5-3. Float](#5-3-Float)
>
> [5-4. Flexbox](#5-4-Flexbox)
>
> [Tip. CSS 파일 최초 생성시 초기화](#CSS-파일을-만들-때-최상단에)
>
> [5-5. Bootstrap](#5-5-Bootstrap)
>
> >[5-5-1. spacing](#5-5-1-spacing)
> >
> >[5-5-2. Color, Text](#5-5-2-Color-Text)
> >
> >[5-5-3. Display, Position](#5-5-3-Display-Position)
> >
> >[5-5-4. Components](#5-5-4-Components)
> >
> >[5-5-5. Grid System](#5-5-5-Grid-System)

<br>

## 1. 웹 사이트의 구성 요소

<br>

- HTML
  - 구조, 뼈대
- CSS
  - 표현
- Javascript
  - 동작

<br>

## 2. 웹 사이트와 브라우저

<br>

- 웹 사이트는 브라우저 위에서 동작함
- 브라우저의 종류가 많아서 각 브라우저의 특성별로 웹 사이트가 조금씩 다르게 동작함
  - 크롬, 파폭, 엣지, 사파리, 오페라 ...
- 그러한 해결책으로 웹 표준이 등장하였다. 
  - 웹에서 표준적으로 사용되는 기술이나 규칙
  - 웹이 똑같이 표시되게 해줌

<br>

## 3. 개발 환경 설정

<br>

- VScode recommended extention
  - Open in browser
  - Auto Rename Tag
  - Auto Close Tag
  - Intellisense for CSS class names in HTML
  - HTML CSS Support
- Chrome developer tools
  - Elements
    - DOM 탐색, CSS 확인 및 변경
      - Styles
        - 요소에 적용된 CSS 확인
      - Computed
        - 스타일이 계산된 최종 결과
      - Event Listeners
        - 해당 요소에 적용된 이벤트 ( Javascript )
  - Sources, Network, Performance, Application, Security, Audits 등

<br>

## 4. HTML 기초

<br>

**H** yper

**T** ext

**M** arkup

**L** anguage

<br>

- Hyper Text
  - 사용자가 하이퍼링크를 통해 문서간에 즉시 접근이 가능한 텍스트
- Markup Language
  - 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
    - HTML
    - Markdown

<br>

### 4-1. HTML 기본 구조

<br>

- 웹 페이지를 구조화하기 위한 언어

- .html 형식의 파일

- 베이직한 형태

  ```html
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>Document</title>
      </head>
      <body>
          <h1>
              웹 문서
          </h1>
          <ul>
              <li>HTML</li>
              <li>CSS</li>
          </ul>
      </body>
  </html>
  ```

  - 기본 규칙
    - 태그당 줄 바꿈 이후 두 칸씩의 공백 (tap)을 주어야 함
    - 따옴표 대신 쌍따옴표
    - = (equal) 앞뒤로 공백을 주지 않는다.

<br>

#### 4-1-1. html

<br>

- 문서의 최상위 (root) 요소

<br>

#### 4-1-2. head

<br>

- 문서 메타데이터 요소

  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용

  <br>

- `<title>` 브라우저 상단 타이틀

- `<meta>` 문서 레벨 메타데이터 요소

- `<link>` 외부 리소스 연결요소

  - CSS 파일
  - favicon 등

- `<script>` 스크립트 요소

  - Javascript 파일, 코드

- `<style>` CSS 직접 작성

  <br>

- 예시

  ```html
  <head>
      <title>HTML 수업</title>
      <meta charset="UTF-8">
      <link href="style.css" rel="stylesheet">
      <script src="javascript.js"></script>
      <style>
          p {
              color: black;
          }
      </style>
  </head>
  ```

<br>

- Open Graph Protocol
  - 메타 데이터를 표현하는 새로운 규약
    - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
    - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의

<br>

#### 4-1-3. body

<br>

1. 문서 본문
   - 실제 화면이 구성되는 곳

2. element

   - 태그와 내용으로 구성되어 있다.

   - `<h1> contents </h1>`

   - 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
     - 요소는 태그로 컨텐츠를 감싸는 것으로 그 정보의 성격과 의미를 정의
     - 내용이 없는 태그도 있다.
       - `br`
       - `hr`
       - `img`
       - `input`
       - `link`
       - `meta`

   - 요소는 중첩될 수 있음
     - 요소의 중첩을 통해 하나의 문서를 구조화
     - 여는 태그와 닫는 태그의 쌍을 잘 확인해야 한다.
       - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨져버린다.
         - 디버깅이 힘들어진다.

3. attribute

   - `<a href="구글"></a>`
   - `href` 속성명
   - `구글` 속성값
   - HTML Global Attribute
     - 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성
       - `id` 문서 전체에서 유일한 고유 식별자 지정
         - PK 처럼 유일한 값을 지정할 때 써야한다.
       - `class` 공백으로 구분된 해당 요소의 클래스의 목록
         - CSS, JS 에서 요소를 선택하거나 접근
       - `data-*` 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
       - `style` inline 스타일
       - `title` 요소에 대한 추가 정보 지정
       - `tabindex` 요소의 탭 순서
     - 몇몇 요소에는 아무 효과가 없을 수 있음

4. Rendering

   - 코딩된 명령들이 전달되어 실제 보이는 사이트로 변하는 과정
   - Document Object Model 트리
     - 텍스트파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조

5. 인라인 / 블록 요소

   - 인라인 요소는 글자처럼 취급
   - 블록 요소는 한 줄 모두 사용

6. 텍스트요소

   - `a` 하이퍼링크
   - `b` `strong` 볼드체
   - `i` `em` 이텔릭체
   - `br` 줄바꿈
   - `img` 이미지
   - `span` 인라인 컨테이너

7. 그룹 컨텐츠

   - `p` 문단
   - `hr` 수평선
   - `ol` `ul` 
     - 리스트
     - ordered / unordered
   - `pre`
     - HTML 에 작성한 내용을 그대로 표현
     - 보통 고정폭 글꼴이 사용되고 공백문자를 유지
   - `blockquote`
     - 인용문
     - 주로 들여쓰기 한 것으로 표현됨
   - `div` 블록 컨테이너

<br>

[목차로 가기](#목차)

<br>

### 4-2. HTML 태그

<br>

#### 4-2-1. 시맨틱 태그

<br>

- 의미부여 요소
  - Non semantic
    - `div`
    - `span`
  - semantic
    - `header`
    - `nav`
    - `aside`
      - 문서 사이드 공간
      - 메인과 관련이 적은 것들
    - `section`
      - 문서의 구분단위
    - `article`
      - 문서 안에서의 구분단위
    - `footer`
- 시맨틱 태그를 사용해야 하는 이유
  - 각 정보들을 알맞은 의미단위로 구분할 수 있음
  - 따라서 코드의 가독성이 좋아지고 유지보수가 쉬워짐
  - 검색 엔진 최적화 (SEO) 를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용해야 한다.

<br>

#### 4-2-2. Table

<br>

- 테이블의 각 부분
  - `<thead>`
  - `<tbody>`
  - `<tfoot>`
  - 그리고 테이블에  대해 `<caption>` 로 설명
- `<tr>` 로 가로 줄을 구성하고 내부에는 `<th>` 혹은 `<td>` 로 셀을 구성
  - `<tr>` 테이블 행
  - `<th>` 테이블 헤드
    - `<thead>` 에 들어가는 데이터는 `<th>` 로 씀
    - `<tbody>` 혹은 `<tfoot>`에 들어가는 경우 그냥 `<td>` 이다.
  - `<td>` 테이블 데이터
- `<colspan>`, `<rowspan>` 속성을 활용하여 칸의 모양을 조작할 수 있다.

<br>

#### 4-2-3. form

<br>

- 데이터를 서버에 주기 위해 사용하는 태그
- 기본 속성
  - action
    - 폼을 처리할 서버의 주소
    - `/search` 같이 써줌
  - method
    - 폼을 제출할 때 사용할 HTTP 메서드
    - `GET` 이나 `POST`
  - enctype
    - 메소드가 post 인 경우 데이터의 유형
    - application/x-www-form-utlencoded
      - 기본값
    - multipart/form-data
      - 어떤 파일을 전송할 때
      - 즉 input type 이 파일인 경우
  - `<form action="/search" method="GET">``</form>`
    - 위와 같이 쓴다.

<br>

#### 4-2-4. input

<br>

- 어떤 데이터가 입력될 때 그 데이터의 종류별로 다양한 input 유형이 제공된다.

  - email, password, text 등

- 대표적인 속성

  - name / value

    - 폼 조작시 쓰이는 이름과 값
    - 이름 / 값 쌍으로 전송

  - 그 외 required, readonly, autofocus, autocomplete, disabled 등

  - ```html
    <form action="/search" method="GET">
        <input type="text" name="q">
    </form>
    ```

  - 위와 같이 쓴다.

<br>

1. input label

   - 라벨을 클릭하여 인풋을 클릭한 것과 같은 효과를 낼 수 있음

   - 특히 모바일같이 터치가 부정확 할 수 밖에 없는 환경에서 편하다.

   - `<input>` 에 `id` 를 주고 `<label>` 에는 `for` 속성을 줘서 서로 연관시킨다.

     - ```html
       <label for="인풋 태그의 아이디">입력과 관련된 문구</label>
       <input type="checkbox 혹은 radio" name="입력을 받고 싶은 것의 이름" id="인풋 태그의 아이디"
       ```

2. input 의 다양한 유형들

   1. 일반적인 입력

      - 단순한 입력을 받기 위해 제공된다.
      - text : 단순 글자
      - password : 뭔가를 써도 글자가 보이지 않고 * 같이 기호로 표현
      - email : 이메일 형식만 받음
      - number : min, max, step 을 써서 숫자 범위 설정가능
      - file : accept 속성을 써서 파일 타입 지정 가능

   2. 항목 중 선택

      - 일반적으로 라벨과 같이 쓴다.

      - 동일한 것에 관해 쓸 때는 같은 name 을 쓰고 다른 value 로 구분

        - ```html
          <div>
          <p>checkbox</p>
          <input id="html" type="checkbox" name="language" value="html">
          <label for="html">HTML</label>
          <input id="python" type="checkbox" name="language" value="python">
          <label for="python">파이썬</label>
          <input id="python" type="checkbox" name="language" value="java">
          <label for="java">자바</label>
          <hr>
          </div
          ```

        - checkbox 는 여러 개 선택

        - radio 는 하나만 가능

   3. 기타

      - 다양한 종류의 input 을 위한 picker 를 제공
      - color, date
      - hidden 은 사용자에게 보이지 않는 인풋

<br>

[목차로 가기](#목차)

<br>

## 5. CSS

<br>

1. Cascading Style Sheets

   - 스타일을 지정하기 위한 언어

   - ```html
     h1 {
       color: blue;
       font-size: 15px;
     }
     ```

   - `h1`
     - 선택자, 스타일을 지정하고 싶은 요소
     - 지정하고 중괄호 안에 속성과 값 쌍으로 스타일을 정해준다.

2. CSS 정의 방법

   - 인라인
     - `<h1 style="~~~">Hello HTML</h1>`
     - 해당 태그에 직접 넣는다.
   - 내부 참조
     - `<style>`
     - `head` 에 미리 지정하기
   - 외부 참조
     - CSS 파일을 분리한 것
     - 외부 CSS 파일을 `head` 에서 링크로 불러오기

3. 기초 선택자

   - 요소 선택자
     - HTML 태그 직접 선택
   - 클래스 선택자
     - `.`
     - 해당 클래스가 적용된 항목 선택
   - 아이디 선택자
     - `#`
     - 해당 아이디가 적용된 항목 선택
     - 단일 id 사용하는것이 일반적인 규칙
       - 여러번 사용해도 동작은 하는데 권장되지는 않는다.

4. 스타일 적용 우선순위

   - 레벨에 따라 `id`  >  `class`  >  `tag`
   - 같은 레벨이라면 제일 나중에 선언된 스타일이 적용된다.
     - 위에서 아래 방향으로 선언이 진행됨

<br>

[목차로 가기](#목차)

<br>

### 5-1. CSS 기본 스타일

<br>

- 크기 단위
  - px (픽셀)
  - % (퍼센트)
  - em
    - 상속 영향 받음
    - 지정한 것의 사이즈에 대해 상대적인 배수단위 사이즈
  - rem
    - 상속 영향 없음
    - html 사이즈를 기준으로 배수단위 사이즈
  - viewport
    - 방문 하자마자 보이는 곳
    - viewport 에 따라 사이즈가 결정됨
    - vw
    - vh
    - vmin
    - vmax
- 색상 단위
  - 색상 키워드
    - `background-color: red;`
    - 대소문자 구분 없음
    - 색상을 글자로 씀
  - RGB
    - ` background-color: #000;`
    - `background-color: #000000; `
    - `background-color: rgb(0, 255, 0);`
    - 16진수, 함수형 표기법으로 표현
  - HSL
    - `background-color: hsl(0, 100%, 50%);`
    - 색상, 채도, 명도로 표현
  - alpha 를 붙이면 투명도를 표현
- CSS 문서 표현
  - 텍스트
    - font
      - -family
      - -style
      - -weight
    - letter-spacing
    - word-spacing
    - line-height
  - 컬러, 배경 이미지, 배경 색
  - 기타 태그별 스타일링
    - 목록, 표

<br>

#### 5-1-1. CSS 선택자

<br>

- 유형
  - 기본
    - 전체, 요소 선택
    - 클래스, 아이디, 속성 선택
  - 결합자
    - 자손, 자식 결합
    - 일반, 인접 형제 결합
  - 의사 클래스 / 요소
    - 링크, 동적 의사 클래스
    - 구조적, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자
- 정리
  - 요소
    - HTML 태그 직접선택
  - 클래스
    - `.` 으로 시작하며 해당 클래스가 적용된 항목 선택
  - 아이디
    - `#` 으로 시작하며 해당 아이디가 적용된 항목 선택
    - 하나의 문서에 한번만 쓰자
- 우선순위
  1. 중요도
     - `!important`
     - 코드의 우선순위 체계가 망가지기 때문에 쓰지 않는것이 좋다.
  2. 우선순위
     1. inline
     2. id
     3. class, attribute, pseudo-class
     4. element, pseudo-element
  3. CSS 파일 로딩 순서

- 상속

  - 부모 속성을 자식에게 전달

  - 되는것

    1. Text 관련 요소
       - font
       - color
       - text-align
    2. opacity
    3. visibility

  - 안 되는 것

    1. Box model 관련 요소

       - width, height

       - margin, padding, border

       - box-sizing

       - display

    2. position 관련 요소
       - top / right / bottom / left
       - z-index

<br>

#### 5-1-2. CSS BOX model

<br>

- 원칙
  1. 모든 요소는 box
  2. 위에서 아래로, 왼쪽에서 오른쪽으로
- 모든 요소는 box 형태
- 하나의 box 는 네 개의 영역으로 구성
  - margin
    - 테두리 외부 여백
    - 배경색 지정 불가능
  - border
    - 테두리
  - content
    - 글, 이미지 등의 내용
  - padding
    - 테두리 내부 여백
    - 배경색, 이미지가 padding 까지 적용된다.
- box-sizing
  - 모든 요소의 box-sizing 은 content-box
    - 즉 padding 을 제외한 순수 contents 영역만을 box 로 지정
    - 우리의 일반 사고방식으로는 경계선까지의 너비를 지정하게 되기 때문에,
    - 이와 같은 경우 box-sizing 을 border-box 로 설정한다.

<br>

#### 5-1-3. CSS Display

<br>

- 원칙
  - 요소들은 display 에 따라 크기와 배치가 달라진다.
- 대표적인 display
  - block
    - 줄 바꿈을 시킨다.
    - 화면 전체의 가로를 혼자 쓴다.
      - 100% 의 영역을 가진다.
      - 가질 수 없다면 그 만큼 자동으로 margin 이 생긴다.
    - 블록 안에 인라인을 넣을 수 있다.
  - inline
    - 줄 바꿈 안되고 행 안에 포함됨
    - content 너비만큼 가로폭을 쓴다.
    - width, height, margin-top, margin-bottom 을 지정할 수 없다.
    - 상하 여백은 line-height 로 지정
- 블록 요소
  - `div`
  - `ul`, `ol`, `li`
  - `p`
  - `hr`
  - `form`
- 인라인 요소
  - `span`
  - `a`
  - `img`
  - `input`, `label`
  - `b`, `em`, `i`, `strong`
- 속성에 따른 수평 정렬
  - `margin-right: auto;` == `text-align: left;`
  - `margin-left: auto;` ==  `text-align: right;`
  - `margin-right: auto; / margin-left: auto;` == `text-align: center;`
- display
  - inline-block
    - block 과 inline 의 특징을 모두 가짐
    - inline 처럼 한 줄에 표시할 수 있다.
    - block 처럼 width, height, margin 속성을 모두 지정할 수 있다.
  - none
    - 해당 요소를 표시하지않고 공간도 주지 않는다.
    - 비슷한 것들 중 hidden 은 공간은 주지만 보여주지는 않는다.

<br>

#### 5-1-4. CSS Position

<br>

- 문서상에서 요소의 위치 지정
- static
  - 모든 태그의 기본 위치
  - 일반적인 요소의 배치순서임
  - 부모 요소 내에서 배치될 때는 부모 위치를 기준으로.
- 좌표 프로퍼티를 사용하여 이동 가능한 것들
  - relative
    - 상대 위치
    - 자기 자신의 static 위치를 기준으로 자신의 모양만 이동
    - 자신이 실제 차지하고 있는 공간은 static 때와 변하지 않았다.
    - 즉 일반적인 흐름을 유지하면서 사람 눈에만 변해 보이게 하는 것
  - absolute
    - 절대 위치
    - 일반적인 문서 흐름에서 빼버림
    - 레이아웃에서 가지고 있는 공간이 없다.
    - static 이 아닌 가장 가까이 있는 부모 / 조상 요소를 기준으로 이동
    - 없는 경우 브라우저 화면 기준으로 이동
  - fixed
    - 고정 위치
    - 일반적인 문서 흐름에서 빼버림
    - 레이아웃에서 가지고 있는 공간이 없다.
    - 부모와 상관없이 viewport 를 기준으로 이동
      - 즉, 스크롤 할 때도 항상 같은 곳에 고정되어있음.
  - sticky
    - 스티커
    - 스크롤에 따라 static 이었다가 fixed 로 바뀜
    - 평소에는 문서에서 static 과 같이 일반적인 문서 흐름에 따른다.
    - 스크롤 위치가 점차 바뀌면서 어느 순간부터는 fixed 처럼 화면에 고정이 되어버림.
- 실제 사용 예시
  - absolute
    - CSS 기본 원칙을 무시하고 특정 영역 위에 요소를 배치하고 싶을 때
    - 부모를 기준으로 어딘가에 배치시킴
  - fixed
    - CSS 기본 원칙을 무시하고 특정에 요소를 배치하고 싶을 때
    - 브라우저를 기준으로 위치시킴
  - sticky
    - 스크롤에 따라 fixed / static
    - 보통 navi 같은곳에 쓰임
- 정리
  - 일반적인 흐름
    1. 모든 요소는 네모
    2. 좌상단부터 배치
    3. display 에 따라 크기 / 배치가 달라짐
  - 위치
    - position 으로 위치되는 기준을 변경
      - relative
        - 자기 원래자리
      - absolute
        - 어떤 부모의 위치
      - fixed
        - 화면의 위치
      - sticky
        - static ~ fixed 가변

<br>

[목차로 가기](#목차)

<br>

### 5-2. CSS Layout

<br>

- 여러 레이아웃 관련 기술들
  - Display
  - Position
  - Float
  - Flexbox
  - Grid
  - 기타 등등

<br>

### 5-3. Float

<br>

- CSS 배치의 기본 원칙에 관해,
  - 박스를 왼쪽이나 오른쪽으로 이동시킨 다음 텍스트를 포함한 인라인 요소들이 그 주변을 감싸도록 함
  - 일반적인 흐름에서 벗어난다.
  - 신문기사 본문과 사진의 구성처럼 됨

<br>

### 5-4. Flexbox

<br>

- 행과 열 형태로 배치시킨다.

- 일반적으로,

  - 가로 main axis
  - 세로 cross axis

- 그 축으로 둘러싸인 박스에 대해,

  - 부모 요소 flex container
    - 레이아웃을 형성하는 기본모델
    - 아이템들이 들어있는 곳
    - 부모 요소로 쓸 것의 display 속성을 flex 혹은 inline-flex 로 지정
      - 그 안의 자식 요소 flex item
      - 컨테이너 안에 있는 컨텐츠

- Flexbox 의 장점

  - 수동적인 값의 부여 없이
    1. 수직 정렬이 가능하다.
    2. 아이템의 너비와 높이 혹은 간격을 동일하게 배치할 수 있다.

- Flex 속성들

  - 배치에 관해,

    1. flex-direction

       - Main 축의 방향을 설정

       - 즉, 요소가 나열되는 방향을 정해준다.

         - row

         - row-reverse

         - column

         - column-reverse

    2. flex-wrap

       - 아이템이 컨테이너 안에 있도록 설정해줌
       - 요소들을 강제로 한 줄에 배치 할 것인지 여부 설정
         - nowrap
           - 기본값
           - 한 줄에 배치
         - wrap
           - 넘치면 그 다음줄로 배치

    - flex-flow
      - direction 과 wrap 의 shorthand
      - `flex-flow: row nowrap;` 처럼 direction 과 wrap 에 대한 설정값을 차례대로 작성

  - 공간 나누기

    1. justify-content
       - main 기준
         - flex-
           - start
           - end
         - center
         - space-
           - between
           - around
           - evenly
    2. align-content
       - cross 기준
         - flex-
           - start
           - end
         - center
         - space-
           - between
           - around
           - evenly

  - 정렬

    - align-items
      - 모든아이템을 cross 기준
        - stretch
        - flex-
          - start
          - end
        - center
        - baseline
          - 써 있는 글자들을 기준으로 기준선을 잡는다.
          - a, b, c, d 글자의 높낮이가 다 다름.
    - align-self
      - 개별 아이템
      - 이 속성은 컨테이너에 적용되는 것이 아니다.
        - stretch
        - flex-
          - start
          - end
        - center

  - 기타 속성

    - flex-grow
      - 남은 공간을 각 요소에 나눠준다.
      - order
        - 배치 순서
      - 예시 `<div class="flex-item grow-1 order-3">`

---

###### CSS 파일을 만들 때 최상단에,

```css
* {
    box-sizing: border-box;
}
body {
    margin: 0;
}
```

###### 이렇게 초기화를 해준다.

---

<br>

[목차로 가기](#목차)

<br>

### 5-5. Bootstrap

<br>

- 미리 만들어져 있는 CSS 파일
- 다운로드 방식과 CDS 방식이 있음

<br>

#### 5-5-1. spacing

<br>

- `mt-3` 과 같이 씀
- m 은 margin
- t 는 top
- 3 은 사이즈
  - 3 이 1rem 으로 기준 크기이다.
  - 0 부터 5 까지와 auto 가 있음
  - bootstrap 으로 마진을 주는 과정에서 important 가 쓰인다.
- 마진, 패딩 그리고 가로세로 방향, 사이즈 등을 정할 수 있다.

<br>

#### 5-5-2. Color, Text

<br>

- Color
  - 기존에 쓰이던 색을 좀 더 시각적으로 부드럽게 다듬어준다.
  - 각 상황별로 쓰이는 색을 미리 설정해두었음
- Text
  - 정렬 관련하여 설정 가능
  - 링크 걸기
  - font-weight, italic 등

<br>

#### 5-5-3. Display, Position

<br>

- 사람들이 많이 쓰는 디자인 패턴을 하나의 모듈화 시켜서 준비해놓음
- 네비게이션 바 같은 경우 기본적으로 준비되어 있는 코드가 있다.
- 그 외 Display, Position 자주 쓰이는 코드들이 재가공되어 준비돼있음.

<br>

#### 5-5-4. Components

<br>

- 검색으로 Bootstrap 의 다양한 UI 요소들 중 원하는 요소를 찾을 수 있음
- 기본 제공된 Components 를 변환해서 사용
  - Buttons
    - 클릭 했을 때 이벤트가 일어남
  - Dropdowns
    - 눌렀을 때 아래로 스크롤이 내려오는 옵션 메뉴처럼 활용
  - Forms, Form controls
    - 로그인, 회원가입, 게시판 등
  - Navbar
    - 네비게이션
  - Carousel
    - 콘텐츠 순환 슬라이드 쇼
  - Modal
    - 현재 페이지를 보고 있는 사람들과 상호작용하기 위해 사용된다.
    - 보고 있는 페이지 위로 레이어가 띄워진다.
    - 페이지를 이동했을 때 사라지게 하거나, 배경을 클릭했을 때 사라지게 하는 등 다양한 옵션이 있음
    - 이것은 자바스크립트를 활용한다.

<br>

#### 5-5-5. Grid System

<br>

- flexbox 로 제작됨
- 요소들을 배치할 때 유용한 시스템
- container >>> row >>> column 으로 배치
- 구성 요소
  - Column
    - 실제 컨텐츠가 들어감
  - Gutter
    - 열과 열 사이 빈 공간
    - 마진처럼 간격
  - Container
    - 열 들이 들어가는 공간
  - 12개의 column 과 6개의 grid breakpoints

<br>

[목차로 가기](#목차)

<br>
