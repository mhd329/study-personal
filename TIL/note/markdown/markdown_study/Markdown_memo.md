# Markdown







## 0. 목차







1. [마크다운의 이론적 이해](#1-마크다운의-이론적-이해)

   

   1. [마크다운이란?](#1-마크다운이란)
   2. [마크다운 특징](#2-마크다운-특징)
   3. [활용 예 - README.md](#3-활용-예---readmemd)

   

2. [마크다운의 문법](#2-마크다운의-문법)

   

   1. [Heading](#1-heading)
   
   2. [Fenced Code block](#2-fenced-code-block)
   
   3. [Inline Code block](#3-inline-code-block)
   
   4. [Link](#4-link)
   
   5. [Image](#5-image)
   
   6. [Blockquotes](#6-blockquotes)
   
   7. [Table](#7-table)
   
   8. [Text](#8-text)
   
   9. [Horizontal Rules](#9-horizontal-rules)
   
   10. [Typora Tip](#10-typora-tip)
   
       
   

​	[참고자료들](#참고자료들)







## 1. 마크다운의 이론적 이해







### 1. 마크다운이란?



- 텍스트 기반의 가벼운 마크업언어 이다.



### 2. 마크다운 특징



- 다양한 환경에서 변환이 되어 문제없이 잘 보여진다.



### 3. 활용 예 - README.md



- Github 같은 곳 에서는 파일명이 README.md 인 것을 모두 보여준다.
  - 오픈소스 공식 문서를 작성하는데 활용 가능하다.
  - 개인 프로젝트 소개서같은 것으로 사용 가능하다.
  - 일종의 설명서로 다양하게 활용될 수 있다.

- Notion 같은 메모 SW 에서도 기본문법으로 마크다운을 쓰고있다.







## 2. 마크다운의 문법







### 1. Heading



- 문서의 제목, 소제목으로 활용
  - '#' 의 개수마다 대응되는 수준이 있다.
  - HTML의 h1 ~ h6 까지 표현 가능하다.
  - 문서 구조적인 구분을 위한 것이기 때문에 크기 조절용으로 사용하기에는 부적절하다.
  - 마크다운으로 헤딩을 표현할 때 띄어쓰기를 해야한다.



### 2. Fenced Code block



- 코드 블록은 ``` 백틱기호 세 개를 활용하여 작성한다.
- 특정 언어를 명시하면 구문 강조가 가능하다.
  - 일부 환경에서는 적용이 안될수 있다.



### 3. Inline Code block



- 코드 블록은 ` 백틱기호 한 개를 인라인에 활용하여 작성한다.



### 4. Link



- "\[문자열](url)" 기능을 통해 링크 작성이 가능하다.
- 특정한 파일들을 포함하여 연결시킬 수도 있다.
- 문서 내부에서 링크하는 방법
  - 목차를 만들 때, \[목차이름](#이동하려는 문서 이름) 이런 식으로 목차를 만들면 된다.
  - 이동하려는 문서 이름이 예컨데 "2. Fenced Code block" 와 같은 경우,
  - (#2. Fenced Code block) 와 같이 쓰면 안되고,
  - (#2-fenced-code-block) 와 같이,
  - 대문자는 소문자로 바꿔주고, 띄어쓰기와 '.' 같은 특수문자 들을 빼고 '-' 를 넣어주어야 한다.
  - 만약 이동하려는 문서 이름에 "활용 예 - README.md" 와 같이 미리 '-' 가 들어가 있었다면,
  - (활용-예---readmemd) 와 같이 기존에 있던 '-' 를 빼지 않고 그대로 쓴다.




### 5. Image



- "\[문자열](url)" 을 통해 이미지 사용 가능하다.
- 특정 파일들을 포함하여 연결시킬 수도 있다.



### 6. Blockquotes



- '>' 를 통해 인용문을 작성할 수 있다.



### 7. Table



- 표는 아래와 같은 구조를 가진다.

  | Syntax    | Description |
  | --------- | ----------- |
  | Header    | Title       |
  | Paragraph | Text        |

- "Ctrl + T" 단축키를 이용하여 만들 수 있다.
  - 일부 지원 안되는 환경도 있다.



### 8. Text



- bold, Italic 을 통해 문자, 문자열을 강조할 수 있다.



### 9. Horizontal Rules



- 세 개 이상의 asterisk \***, dashes \---, underscores \___



### 10. Typora Tip



- Image는 아래의 설정을 해 두면 마크다운 파일이 있는 위치에 md-images 폴더를 만들고, 가능한 이미지들을 모두 복사하여 상대경로로 표현함
  - 상대경로 예시 : ./md-images/untitle.png
  - 절대경로 예시 : C:/Users/mhd32/Desktop/TIL/untitle.png
- 백슬래시 '\\' 를 쓰면 문법에 적용되는 특수기호가 일반 글자처럼 취급이 된다.







## 참고자료들







- [깃허브 마크다운 정리글](https://gist.github.com/ihoneymon/652be052a0727ad59601)



- [마크다운 위키백과](https://ko.wikipedia.org/wiki/%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4)







---

###### 본문 최종수정일자 : 2022-07-06
