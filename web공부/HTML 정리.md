# HTML

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

## 5. HTML 기본 구조

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

### 5 - 1. html

<br>

- 문서의 최상위 (root) 요소

<br>

### 5 - 2. head

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

### 5 - 3. body

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

## 6. CSS 기초

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

---

###### 웹 접근성 체험

- 웹을 이용하는 여러 사람들이 모두 나와 같은 일반인만 있을 것이라고 무의식적으로 생각하고 있었는데 그렇지 않은 사람들도 사용하고 있다는 것을 느꼈다.
- 몸에 장애가 있는 사람들을 돕기 위해 특별하고 대단한 기술이 필요하지 않고 약간의 아이디어 만으로 가능하다는 것을 깨달았다.
- 이러한 기술은 각종 장애를 가진 사람들에게만 유효하게 쓰이는 것이 아니라 특정 상황에서는 비 장애인에게도 충분히 유용한 기능이 될 수도 있겠다는 생각을 했다.
