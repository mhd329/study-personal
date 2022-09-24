# Django 정리

<br>

## 목차

<br>

[1. 인터넷 기초](#1-인터넷 기초)

>[1-1. 클라이언트와 서버](#1-1-클라이언트와 서버)
>
>[1-2. 웹 브라우저와 웹 페이지](#1-2-웹 브라우저와 웹 페이지)

[2. Django 개요](#2-Django-개요)

>[2-1. 소프트웨어 디자인 패턴](#2-1-소프트웨어-디자인-패턴)
>
>[2-2. Django 의 디자인 패턴](#2-2-Django-의-디자인-패턴)
>
>[2-3. Django 구성요소](#2-3-Django-구성요소)

[3. Django 요청과 응답](#3-Django-요청과-응답)

>[3-1. Django Template](#3-1-Django-Template)
>
>> [3-1-1. Variable](#3-1-1-Variable)
>>
>> [3-1-2. Filters](#3-1-2-Filters)
>>
>> [3-1-3. Tags](#3-1-3-Tags)
>>
>> [3-1-4. Comments](#3-1-4-Comments)

<br>

## 1. 인터넷 기초

<br>

- web
  - 전 세계는 해저 케이블 같은 유선의 형태로 이어져 있다.
  - 위성 같은 무선으로도 이어지고 있다.
  - 마치 거미줄처럼 다양한 통신망으로 연결되어 있다.

<br>

### 1-1. 클라이언트와 서버

<br>

- 오늘날 대부분 웹 서비스는 클라이언트 - 서버 구조
  - 클라이언트와 서버는 결국 하나의 컴퓨터이다.
  - 클라이언트는 request 를 보낸다.
  - 서버는 request 를 받고 response 를 보낸다.

- 클라이언트는 서버를 요청하는 주체
  - 웹을 사용하는 사용자 혹은 사용자의 웹 브라우저
  - 웹 사용자의 인터넷에 연결된 장치
- 서버는 요청에 대해 서비스를 응답하는 주체
  - 웹 페이지 데이터를 응답해 사용자 웹 브라우저에 표시되게 해줌
  - 웹 페이지, 사이트, 앱을 저장하는 컴퓨터

<br>

### 1-2. 웹 브라우저와 웹 페이지

<br>

- 웹 브라우저
  - 웹에서 페이지를 찾아 보여주고 사용자가 하이퍼링크를 통해 다른 페이지로 이동할 수 있도록 도와주는 프로그램
  - 웹 페이지 파일을 렌더링해주는 프로그램
  - 서버로부터 전달받은 HTML/CSS 파일과 JavaScript 를 조립해서 화면에 띄워준다.
- 웹 페이지
  - 사용자가 웹에서 보는 화면
  - 정적 웹 페이지와 동적 웹 페이지가 있다.
- 정적 페이지
  - Static Web page
  - 있는 그대로의 페이지
  - 한 번 작성된 HTML 파일의 내용이 변하지 않는다.
- 동적 페이지
  - Dynamic Web page
  - 요청에 따라 서버에 의해 추가적인 수정이 되어 보여지는 페이지

<br>

[위로가기](#목차)

<br>

## 2. Django 개요

<br>

- 웹 프레임워크
  - 웹 서비스 개발을 위해 만들어진 web framework
  - 웹 개발에 필요한 기능들 중 자주 쓰이는 기능들을 따로 모아 유지관리하는 작업도구이다.
  - 소프트웨어의 생산성과 품질을 높임

<br>

### 2-1. 소프트웨어 디자인 패턴

<br>

- 현업에서 프로그램을 구조화 할 때 작업 효율성에 따라 자주 사용되는 몇 가지의 디자인 패턴이 생겨나게 되었다.
- 그것들을 일반화해서 하나의 공법으로 만든 것이다.
  - 다양한 응용 소프트웨어를 개발할 때 종류 무관 항상 등장하는 공통적인 설계 문제가 등장한다.
  - 이를 해결하는 방법에도 공통점이 있다는 것이 발견되었다.
    - 이러한 유사점을 패턴이라 한다.
    - 클라이언트 - 서버 구조도 패턴의 일종
    - 패턴화 함으로써 어떤 공통적인 문제들의 해결이 수월해진다.
    - 개발 방법론을 표준화 함으로써 복잡성이 줄어든다.

<br>

### 2-2. Django 의 디자인 패턴

<br>

- Django 의 경우 MTV 패턴이 적용되어 있다.
  - MVC 패턴이 조금 변형된 것
    - Model : 데이터 처리
    - View : 화면 처리
    - Controller : 모델과 뷰 연결
  - MTV 패턴
    - Model
    - Template : MVC 의 View 에 해당
    - View : Controller 에 해당

<br>

### 2-3. Django 구성요소

<br>

- 프로젝트 구조
  - `__init__.py`
    - 파이썬에게 직접 지시하는 파일
    - 별도의 추가 코드 작성하지 않음
  - `asgi.py`
    - Django 애플리케이션이 비동기식 웹 서버와 소통하는 것을 도움
  - `settings.py`
    - Django 프로젝트 설정 관리
  - `urls.py`
    - 사이트 url 과 적절한 view 의 연결을 지정
  - `wsgi.py`
    - Django 애플리케이션이 비동기식 웹 서버와 소통하는 것을 도움
  - `manage.py`
    - Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

<br>

- 애플리케이션 구조
  - `admin.py`
    - 관리자 페이지 설정
  - `apps.py`
    - 앱 정보가 작성된 곳
    - 별도 추가 작성은 필요가 없다.
  - `models.py`
    - Model 을 정의하는 곳
  - `tests.py`
    - 프로젝트의 테스트코드를 작성하는 곳
  - `views.py`
    - view 함수들이 정의되는 곳

---

###### 앱 사용을 위해서는 반드시 settings.py 의 INSTALLED_APPS 리스트에 앱의 이름을 추가해야 한다.

```python
# settings.py

INSTALLED_APPS = [
'앱 이름',
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
]
```

###### 늦게 만들어지는 순서로 위로 올려가면서 작성해간다.

---

- project
  - 앱의 집합
- Application
  - 요청을 처리하고 페이지를 보여줌
  - 하나의 역할 단위로 작성하는것이 권장된다.

<br>

[위로가기](#목차)

<br>

## 3. Django 요청과 응답

<br>

- URL - VIEW - TEMPLATE
  - `urls.py` - `views.py` - `templates` 디렉토리의 html 파일

<br>

- `views.py`
  - HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
  - Template 에게 HTTP 응답 서식을 맡김
  - `render()`
    - `render(request, template_name, context)`
    - 주어진 템플릿을 주어진 컨텍스트 데이터와 결합
    - 렌더링 된 텍스트와 함께 HttpResponse 객체를 반환하는 함수
      - `request`
        - 응답을 생성하는 데 사용되는 요청 객체
      - `template_name` 
        - 템플릿의 전체 이름 또는 템플릿 이름의 경로
      - `context`
        - 템플릿에서 사용할 데이터
        - 딕셔너리 타입으로 작성
- `templates`
  - 실제 내용을 보여주는 `.html` 파일이 들어가는 디렉토리
  - 파일 구조나 레이아웃을 정의
  - `template` 파일의 기본 경로
    - `app`
      - `templates`
        - `.html`
- 추가 설정
  - `settings.py`
    - `LANGUAGE_CODE = 'ko-kr'`
      - 모든 사용자에게 제공되는 번역을 결정
      - [USE_I18N](http://www.i18nguy.com/unicode/language-identifiers.html) `== True` 인 경우에만 적용됨
        - Django 의 번역 시스템을 활성화 할 것인지의 여부
    - `TIME_ZONE = 'Asia/Seoul'`
      - DB 연결의 시간대를 나타내는 문자열 지정
      - [USE_TZ]([List of tz database time zones - Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)) `== True`
        - datetimess 가 기본적으로 시간대를 인식하는지의 여부
        - UTC 대신 새로 설정한 시간대의 날짜와 시간이 반환됨
        - `True` 인 경우 Django 는 내부 시간대의 날짜와 시간을 사용
        - `False` 인 경우 error 발생
    - USE_L10N
      - data 의 localized formatting 을 활성화할지 여부
      - `True` 인 경우 Django 는 현장의 형식을 사용하여 숫자와 날짜를 표시

<br>

[위로가기](#목차)

<br>

### 3-1. Django Template

<br>

- 표현 제어 도구, 로직
- HTML 정적 부분과 동적 컨텐츠 삽입
- Django Template Language
  - DTL Syntax
    - Variable
    - Filters
    - Tags
    - Comments
  - Django 에서 사용하는 built-in template system
  - 조건, 반복, 변수 치환, 필터 등의 기능을 제공
    - Python 의 if, for 문과 같은 일부 프로그래밍 구조를 사용할 수 있음
    - 그러나 Python 코드로 실행되는 것은 아니다.
    - 단순하게 Python 이 HTML 로 들어간 것이 아니다.
  - 프로그래밍 언어가 아니라 어떤 자료를 표현하기 위한 방법의 하나일 뿐이다.

<br>

#### 3-1-1. Variable

- `{{ variable }}`
- 변수명은 영어, 숫자와 밑줄의 조합으로 구성될 수 있으나 밑줄로는 시작할 수 없다.
  - 공백이나 구두점도 사용 불가
- `.` 을 사용하여 변수 속성에 접근할 수 있음
- `views.py` 파일 내부 함수의 반환값 중 `render()` 의 세 번째 인자인 `context` 에 딕셔너리 형태로 넘겨준다.
  - 넘겨진 딕셔너리의 `key` 에 해당하는 문자열이 template 에서 사용 가능한 변수명이 된다.

<br>

#### 3-1-2. Filters

<br>

- `{{ variable|filter }}`
- 표시할 변수를 조건에 맞게 가공할 때 사용
- `{{ name|lower }}`
  - `name` 변수를 모두 소문자로 출력
- 60개의 필터링 옵션이 있다.
- chained 가 가능하며 일부 필터는 인자를 받기도 한다.
  - `{{ name|truncatewords:30 }}`

<br>

#### 3-1-3. Tags

<br>

- `{% tag %}`
  - 출력 텍스트 만들기
  - 반복문, 논리제어를 통하여 제어의 흐름 만들기
- 변수보다 복잡한 일을 수행한다.
- 일부 태그는 시작과 종료 태그가 필요하다.
  - `{% 태그 이름 %} ~ {% end + 태그 이름 %}`
    - `{% if %} ~ {% endif %}`
- 스물 네 종류의 태그 제공

<br>

#### 3-1-4. Comments

<br>

- `{# ~ #}`
- 한 줄 짜리 주석을 표현하는 데에 사용된다.
- 줄 바꿈은 허용되지 않는다.
- 여러 줄 주석은 `{% comment %} ~ {% endcomment %}` 의 형식으로 사용한다.

<br>

[위로가기](#목차)

<br>

