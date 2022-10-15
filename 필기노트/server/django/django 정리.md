# Django 정리

<br>

## 목차

<br>

[1. 인터넷 기초](#1-인터넷-기초)

>[1-1. 클라이언트와 서버](#1-1-클라이언트와-서버)
>
>[1-2. 웹 브라우저와 웹 페이지](#1-2-웹-브라우저와-웹-페이지)

[2. Django 개요](#2-Django-개요)

>[2-1. 소프트웨어 디자인 패턴](#2-1-소프트웨어-디자인-패턴)
>
>[2-2. Django 의 디자인 패턴](#2-2-Django-의-디자인-패턴)
>
>[2-3. Django 구성요소](#2-3-Django-구성요소)

[3. Django 요청과 응답](#3-Django-요청과-응답)

>[3-1. Django Template](#3-1-Django-Template)
>
> > [3-1-1. Variable](#3-1-1-Variable)
> >
> > [3-1-2. Filters](#3-1-2-Filters)
> >
> > [3-1-3. Tags](#3-1-3-Tags)
> >
> > [3-1-4. Comments](#3-1-4-Comments)
> >
> > [3-1-5. 템플릿 상속](#3-1-5-템플릿-상속)
> >
> > [3-1-6. 템플릿 namespace](#3-1-6-템플릿-namespace)
>

[4. Variable routing](#4-Variable-routing)

[5. form](#5-form)

> [5-1. Client](#5-1-Client)
>
> [5-2. Server](#5-2-Server)
>
> >[5-2-1. HTTP 의 요청 방식](#5-2-1-HTTP-의-요청-방식)
> >
> >[5-2-2. CSRF](#5-2-2-CSRF)
> >
> >[5-2-3. csrf_token](#5-2-3-csrf_token)

[6. URL](#6-URL)

> [6-1. App URL mapping](#6-1-App-URL-mapping)
>
> [6-2. 포함 기능](#6-2-포함-기능)
>
> [6-3. URL patterns 이름 부여](#6-3-URL-patterns-이름-부여)

[7. Database](#7-Database)

>[7-1. Model](#7-1-Model)
>
>[7-2. Migrations](#7-2-Migrations)
>
>[7-3. 추가 필드의 정의](#7-3-추가-필드의-정의)
>
>[7-4. ORM](#7-4-ORM)
>
>[7-5. QuerySet API](#7-5-QuerySet-API)
>
> >[7-5-1. CREATE](#7-5-1-CREATE)
> >
> >[7-5-2. READ](#7-5-2-READ)
> >
> >[7-5-3. UPDATE / DELETE](#7-5-3-UPDATE-/-DELETE)

[8. Django ModelForm](#8-Django-ModelForm)

>[8-1. ModelForm 사용방법](#8-1-ModelForm-사용방법)
>
>[8-2. ModelForm 활용 로직](#8-2-ModelForm-활용-로직)
>
>[8-3. ModelForm instance](#8-3-ModelForm-instance)

[9. Admin](#9-Admin)

[10. Static files](#10-Static-files)

[11. Django Auth](#11-Django-Auth)

>[11-1. User model 활용하기](#11-1-User-model-활용하기)
>
>[11-2. 회원 가입](#11-2-회원-가입)

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
- 설계 철학
  - 표현과 로직을 분리
  - 중복을 배제
    - 템플릿 상속의 기초가 되는 철학이다.


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

#### 3-1-5. 템플릿 상속

<br>

- 웹 페이지를 만들 때 반복 사용되는 코드들을 재사용하기 위해 사용
- 코딩 효율을 높여준다.

```html
{% extends "[뼈대 페이지.html]" %}

{% block [공간 이름] %}
자식 템플릿에서 재정의 가능한 공간
{% endblock [공간 이름](생략 가능) %}
```

- extends 는 반드시 템플릿 최상단에 쓰여져야 한다.
- 부모 페이지를 모든 페이지에 상속 할 수 있게 경로를 설정해주어야 한다.
  - 프로젝트 최상단에 templates 디렉토리를 만든다.
  - `뼈대 페이지.html` 를 templates 에 넣는다.
  - `setting.py` 의 `TEMPLATES`  `'DIRS' : []` 에 다음과 같이 쓴다.
    - `[BASE_DIR / "templates"]`
- [pathlib — 객체 지향 파일 시스템 경로 — Python 3.9.14 문서](https://docs.python.org/ko/3.9/library/pathlib.html#module-pathlib)

<br>

#### 3-1-6. 템플릿 namespace

<br>

- Namespace
  - 개체를 구분할 수 있는 범위이다.
  - URL namespace 를 사용하면 서로 다른 앱에서도 문제없이 동일한 URL 로 사용할 수 있다.
    - `app_name` 변수를 만들어서 URL namespace 를 설정해야 한다. 
      - `app_name = [해당 앱의 이름]`
      - url 주소의 변화 `{% url 'url 이름' %}  {% url '[앱 이름]:[url 이름]' %}`
      - `app_name` 을 지정한 후 부터는 url 태그에서 반드시 `[앱 이름]:[url 이름]` 형식으로 사용해야 한다.

- 장고는 기본적으로 `[앱 이름]/templates/` 경로에 있는 html 파일만 찾을 수 있다.
- 그것은 settings.py 의 INSTALLED_APPS 에 **[앱] 이 작성된 순서대로** html 을 검색 후 렌더링한다.
- 디렉토리를 따로 생성해 물리적으로 namespace 에 구분을 줄 수 있다.
  - 장고 템플릿의 기본 경로를 바꿀 수는 없다.
  - 대신 `[앱 이름]/templates/[앱 이름]/` 형태로 만들 수 있다.
- 이름공간의 구조가 바뀌었으면 urls.py 등 해당하는 모든 경로도 전부 수정해주어야 한다.

<br>

[위로가기](#목차)

<br>

## 4. Variable routing

<br>

- url 의 일부분을 변수로 지정하여 view 함수의 인자로 넘길 수 있음
- 변수값에 따라 주소가 바뀌고 그에 해당하는 페이지를 일일이 만들지 않아도 된다.
- `path()` 에서 여러 페이지를 연결 시킬 수 있음

```python
urlpatterns = [
	path('hello/<str:name>/', views.hello), # 1
	path('hello/<name>/', views.hello), # 2
]
```

- 기본 타입이 str 이기 때문에 `# 2` 와 같이 작성해도 된다.
  - str
    - `/` 를 제외하고 비어있지 않은 모든 문자열
  - int
    - 0 또는 양의 정수
  - slug
  - uuid
  - path

```python
def index(request, [매개변수]):
    context = {
        "매개변수" : [매개변수]
    }
    return render(request, "index.html", context)
```

```html
<!-- index.html -->
<h1>
    {{ [매개변수] }}
</h1>
```

<br>

[위로가기](#목차)

<br>

## 5. form

<br>

- html \<form> 태그
  - 데이터를 전송하기 위해 사용되는 태그
    - `action`
      - 데이트를 보낼 url 지정
      - 지정하지 않으면 현재 페이지로 되돌림
    - `method`
      - 전송 방법을 정의
      - 웹의 다양한 자원들을 가져올 수 있도록 해주는 규칙
      - 웹상 데이터 교환의 기초
        - `GET`
          - `method` 를 작성하지 않을 시 기본값
          - 서버로부터 정보를 조회하는데 사용
          - 가져오기 전용
          - `GET` 방식에서는 url 형식으로 데이터를 전달
          - `name` 은 `key` , `value` 는 `value` 로 매핑되어 전달됨
        - `POST`
        - `PUT`
        - `DELETE`

<br>

### 5-1. Client

<br>

- \<form> 태그 등으로 서버에 요청을 보내는 주체

- 브라우저는 url 을 통해 요청을 담아 전송한다.

  - \<form> 태그의 `action` 속성에 url 을 기입한다.

- html \<input> 태그

  - 클라이언트는 \<input> 태그에 양식에 맞는 요청을 추가한 뒤,  \<form> 의 `action` 에서 url 과 결합하여 데이터를 보낸다.
  - `type` 에 따라 동작이 달라진다.
    - 기본값은 `text`
  - `value` 를 작성하면 기본 입력값이 설정된다.
  - `name`

  ```html
  <form action="name 으로 설정된 어떤 이름에 담긴 데이터를 받을 url" method="쓰지 않을 시 기본값 GET">
      <input type="text" name="input 에 어떤 값을 적었을 때 그 값이 담겨진 이름">
  </form>
  ```

  - `GET` 방식으로 전송 시 url 의 변화
    - `~~~/[action 에서 정한 주소]/?[name 에서 정한 이름]=[input 에 적은 값]`
      - 정해진 주소 뒤에 물음표를 쓰는 것으로 시작을 알림
    - `key=value` 쌍이 많은 경우 `&` 로 구분됨
      - 쿼리스트링 이라고도 함

<br>

### 5-2. Server

<br>

- 요청에 맞는 데이터를 가져옴
  - 모든 요청 데이터는 `request` 라는 매개 변수에 들어있다.
- 브라우저의 요청에 대한 응답 과정
  1. 브라우저에 의해 페이지가 요청된다.
  2. django 는 요청에 맞게 데이터를 넣어서 HTTP request object 를 생성
  3. 요청에 해당하는 view 함수를 로드
  4. HTTP request 를 첫 번째 인자로 전달
  5. view 함수는 HTTP response object 를 반환


<br>

[위로가기](#목차)

<br>

#### 5-2-1. HTTP 의 요청 방식

<br>

- `GET` 과 `POST` 가 있다.
- `GET`
  - 무언가를 가져오도록 요청할 때 사용
  - 반드시 가져올 때만 사용해야 한다.
  - DB에 변화를 주지 않음
  - CRUD 에서 오직 R 만을 담당한다.
  - 쿼리 스트링 파라미터 형태로 URL 로 데이터를 보낸다.
    - URL 에 데이터가 표시된다.
    - 보안상 취약할 수 있다.

- `POST`
  - 서버로 데이터를 보낼 때 사용
  - DB에 변화를 준다.
  - CRUD 에서 CUD 를 담당한다.
  - 데이터를 HTTP body 에 담아서 보낸다.
    - URL 로 데이터를 보내지 않는다.


<br>

#### 5-2-2. CSRF

<br>

- Cross - Site - Request - Forgery
- 사이트 간 요청 위조
- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
- 공격 방어법
  - 보안 토큰 사용 방식
    - CSRF Token
      - 사용자의 데이터에 임의의 난수 값을 부여해 매 요청마다 해당 난수값을 포함시켜 전송
      - 전달된 토큰값이 유효한지 검증
    - 일반적으로 DB 변경이 가능한 `POST`, `PATCH`, `DELETE` 등에 적용
- 장고에서는 DTL 에서 csrf_token 탬플릿 태그를 제공한다.

<br>

#### 5-2-3. csrf_token

<br>

- `{% csrf_token %}`
- 어떤 요청에 대해 페이지에 해당 태그가 없다면 장고 서버는 `403 forbidden` 으로 응답한다.
- 템플릿에서 내부 URL 로 향하는 `POST` form 을 사용하는 경우 쓰인다.
  - 내부에서 외부 URL 로 향하는 경우 토큰이 유출될 수 있기 때문에 사용해서는 안된다.

<br>

[위로가기](#목차)

<br>

## 6. URL

<br>

- 클라이언트는 요청사항을 url 을 통해 전달함
- django 는 url 끝에 슬래쉬가 없다면 자동으로 붙여준다.
  - 기술적인 측면에서 `foo.com/bar` , `foo.com/bar/` 는 다르다.
  - url 형태를 통일시켜서 정규화를 해야한다.

<br>

### 6-1. App URL mapping

<br>

- 덩치가 커져갈수록 하나의 urls.py 에 모든 주소를 관리하는 것은 유지보수에 좋지 않다.

- 해결법

  1. 각각의 앱 안에 urls.py 를 만든다.
  2. 경로를 잡아주고 아래와 같이 urls.py 의 형식에 맞게 import 를 해준다.

  ```python
  from . import views # 경로 설정
  from django.urls import path
  
  urlpatterns = [
      
  ]
  ```

<br>

### 6-2. 포함 기능

<br>

- urlpatterns 에는 다른 url 모듈도 들어갈 수 있다.

```python
# 프로젝트 루트 디렉토리의 urls.py

urlpatterns = [
path('admin/', admin.site.urls),
path('articles/', include('articles.urls')),
path('pages/', include('pages.urls')),
]
```

- `include()`
  - 다른 URLconf 들을 참조할 수 있도록 돕는 함수
- `articles/` 와 관련된 주소는 articles 경로 하위의 urls.py 에게 전달된다.
  - URL의 일치하는 부분만 잘라내고 그 후속 부분은 전달받은 다른 urls.py 파일이 조작하게 된다.
- 포함 되는 앱 하위로 urls.py 를 따로 만들었고 루트 디렉토리의 urls.py 에서 include 로 조작하려면,
- 그 앱의 urls.py 에 urlpatterns 가 작성되어있어야 한다.
  - 빈 리스트라도 작성되어 있어야 정상 동작한다.

<br>

### 6-3. URL patterns 이름 부여

<br>

```python
urlpatterns = [
    path('index/', views.index, name='index'),
    path('a/', views.a, name='a'),
    path('b/', views.b, name='b'),
]
```

- 어떤 페이지의 문자열 주소가 변경되는 경우 그 전까지 그 주소로 사용되고있던 모든 문자열 주소를 업데이트 해야 한다.
- `name` 인자를 정의해서 사용 할 경우 원본 urlpatterns 를 자유롭게 변경 할 수 있다.
- `{% url 'url 이름' %}` 형식으로 사용한다.

<br>

[위로가기](#목차)

<br>

## 7. Database

<br>

- 기본 구조
  - Schema
    - 뼈대
    - 자료의 구조, 표현 방법, 관계 등을 정의한 것
    - 데이터는 스키마 형식에 맞게 입력된다.
  - Table
    - Relation 이라고도 부른다.
    - 필드와 레코드로 조직된 데이터 요소들의 집합
      - 필드
        - 속성, 컬럼
        - 스키마에서 지정된 각각의 데이터 형식이 각 행에 맞게 지정된다.
      - 레코드
        - 튜플, 행
        - 데이터가 저장되는 가로줄
        - 하나의 행에는 열의 개수만큼 데이터가 저장된다.
- Primary Key
  - 기본으로 가지는 고유한 id, 중복될 수 없다.
  - 식별자로 사용된다.
  - DB 관리 및 다 DB간의 관계 설정 시 중요하게 쓰인다.
- 쿼리
  - 데이터를 조회하기 위한 명령어

<br>

### 7-1. Model

<br>

- 장고는 모델을 활용하여 데이터를 조작

- 저장된 DB의 레이아웃

- 각각의 모델은 일반적으로 어떤 단일 DB의 테이블 하나에 대응된다.

- 모델 작성법

  - 클래스를 만들고 클래스 변수에 값으로 초기화하는 형태

  ```python
  class [테이블 이름](models.Model):
      [필드 1 이름] = models.[필드 1 의 타입]
      [필드 2 이름] = models.[필드 2 의 타입]
      
  class app(models.Model):
      title = models.CharField(max_length=[값])
      content = models.TextField()
  ```

- 각 모델은 `django.models.Model` 클래스의 서브 클래스이다.
- `models` 모듈을 통해 DB필드의 타입을 정의
  - 다양한 모델 [필드](https://docs.djangoproject.com/en/3.2/ref/models/fields/)가 있다.

<br>

### 7-2. Migrations

<br>

- 주요 명령어
  - makemigrations
    - `python manage.py makemigration`
    - 새로운 DB 설계도를 만들 때 사용
  - migrate
    - `python manage.py migrage`
    - 명령어로 만든 설계도를 실제 DB에 반영
- 기타 명령어
  - showmigrations
    - `python manage.py showmigrations`
    - 기타 명령어
    - 잘 반영 됐는지의 여부 파악 용도
    - `X` 표시가 있으면 잘 된것
  - sqlmigrate
    - ` python manage.py sqlmigrate [앱 이름] [파일 번호] `
    - 해당 설계도가 실제 DB 언어로 어떻게 해석될지 확인할 수 있음

<br>

### 7-3. 추가 필드의 정의

<br>

- 사용 중 models.py 에 변경사항이 생긴 경우 migration 과정
  - 기존 클래스 내부에 추가 모델 필드 작성 후 다시한번 makemigrations 진행
    - `python manage.py makemigrations`
  - 만들어져있던 기존 테이블에 새로운 필드가 추가되려면 거기에 기본으로 추가될 어떤 값이라도 반드시 가지고 있어야 한다.
- DB와 동기화 해서 변경사항을 반영해야 한다.
  - `python manage.py migrate`


<br>

### 7-4. ORM

<br>

- Object-Relational-Mapping
- 객체지향 프로그래밍 언어를 사용하여 다른 언어로 작성된 데이터를 SQL 언어 없이 DB 로 옮길 수 있게 변환시켜주는 기술
- SQL 언어를 잘 몰라도 DB 조작이 가능하다
- 객체 지향적 접근으로 인해 **생산성**이 높아진다.
- 세밀한 조작은 힘들다.

<br>

### 7-5. QuerySet API

<br>

- Query
  - DB 에 특정 데이터를 보여달라는 요청
- QuerySet
  - DB 에서 전달 받은 데이터 모음
  - 순회가 가능한 QuerySet 형태로 가져와진다.
  - 단일 객체를 반환 할 때는 QuerySet 이 아닌 클래스의 인스턴스 형태로 가져와진다.
- CRUD
  - Create, Read, Update, Delete
  - 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 네 가지
  - QuerySet API 를 통해 조작할 수 있다.


<br>

[위로가기](#목차)

<br>

#### 7-5-1. CREATE

<br>

- DB 객체를 만드는 세 가지 방법

- 첫 번째 방법

  - 단계별로 만들기

    1. `[객체 이름] = [클래스 이름]()`
       - 클래스를 통한 인스턴스 생성

    2. `[객체 이름].[필드 이름] = [필드 값]`
       - 필드에 값 할당

    3. `[객체 이름].save()`
       - `.save()` 로 변경사항 저장

- 두 번째 방법

  - 인스턴스 생성 시 초기값을 포함하여 한꺼번에 작성
    1. `[객체 이름] = [클래스 이름]([필드 이름 1] = "[필드 값 1]", [필드 이름 2] = "[필드 값 2]")`
    2. `[객체 이름].save()`

- 세 번째 방법

  - 저장기능이 포함된 `Create()` 메서드를 활용하여 한번에 작성
    - `[객체 이름].objects.create([필드 이름 1] = "[필드 값 1]", [필드 이름 2] = "[필드 값 2]")`

<br>

#### 7-5-2. READ

<br>

- `.all()`
  - 전체 데이터 조회
  - 반환값이 있음
  - `[클래스 이름].objects.all()`
- `.get()`
  - 단일 데이터 조회
  - 객체를 찾을 수 없거나 둘 이상 찾게 되면 예외가 발생
  - 주로 PK 조회에서 사용된다.
  - `[클래스 이름].objects.get()`
- `.filter([필터링 옵션])`
  - 여러 데이터 조회
  - 객체를 찾을 수 없거나 한 개 뿐이어도 QuerySet 을 반환
  - 필터링 [옵션](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups)에 의해 필터링 된 객체들을 QuerySet 형태로 반환

<br>

#### 7-5-3. UPDATE / DELETE

<br>

- 객체 호출 후 필드 값을 변경한 다음 저장
  1. `[객체 이름] = [클래스 이름].objects.get(id=[객체 id])`
  2. `[객체 이름].[필드 이름] = "[새로운 필드값]"`
  3. `[객체 이름].save()`
- 객체 호출 후 삭제
  1. `[객체 이름] = [클래스 이름].objects.get(id=[객체 id])`
  2. `[객체 이름].delete()`

<br>

[위로가기](#목차)

<br>

## 8. Django ModelForm

<br>

- UI 와 DB 사이에서 오고가는 데이터의 형식이 일치하는지 확인하는 절차가 반드시 필요하다.
- HTML Form 과 Django Model 은 UI 와 DB 의 관계
  - 유효성 검증이 필요하다.
  - 서버측에서 필수적으로 처리해야 한다.

<br>

### 8-1. ModelForm 사용방법

<br>

```python
from django import forms
from .models import [모델 이름]

	class [모델 폼 이름](forms.ModelForm):
		class Meta:
			model = [모델 이름]
			fields = "__all__"
```

1. 앱 경로 안에 새로 `forms.py` 파일을 만든다.

2. `class [모델 폼 이름]`으로 새 클래스를 만들면서 `forms` 라이브러리의 `ModelForm` 클래스를 상속받는다.

3. 정의한 클래스 안에 다시 `Meta` 클래스를 선언한다.

4. `Meta` 클래스 내부에 어떤 모델을 기반으로 form 을 만들 것인지에 대한 정보를 기입한다.

   - `model` 속성에 사용할 모델을 할당한다.
   - `fields` 속성에 `"__all__"` 을 쓰면 모델의 모든 필드가 들어감

   - `exclude` 속성을 사용하면 모델에서 포함하지 않을 필드를 지정할 수도 있다.

5. `views.py` 에서 모델 폼을 사용할 함수에 새로운 인스턴스를 만든다.

6. 만들어진 객체를 `context` 에 전달한다.

7. html 문서에서 Input Field 를 사용하여 모델 폼을 생성한다.
   - 폼 렌더링 옵션들
     - `as_p()`
       - 각 필드를 단락으로 감싸기
     - `as_ul()`
       - 각 필드를 리스트로 감싸기
       - `ul` 태그는 직접 작성해야 한다.
     - `as_table()`
       - 각 필드를 테이블로 감싸기


<br>

### 8-2. ModelForm 활용 로직

<br>

- 요청 방식에 따른 분기

  - `GET` 요청을 받았을 때,

    -  모델 폼을 가져온 다음 `context` 에 담아서 페이지에 폼을 렌더링

  - 해당 폼이 있는 페이지 내에서 다시 `POST` 요청을 받았을 때,

    - 요청이 모델 폼의 요구조건에 맞게 작성이 되었는지 유효성 검사

      - 검사 성공 시 DB 에 저장

      - 검사 실패 시 기존 폼의 `context` 내용을 현재 페이지의 Form 으로 다시 전달

- `form` 인스턴스의 `errors` 속성

  - `is_valid()` 의 반환 값이 `False` 인 경우 `form` 인스턴스의 `errors` 속성에 값이 작성된다.
  - 검증 실패의 원인이 딕셔너리의 형태로 작성된다.
    - `form.errors`

<br>

### 8-3. ModelForm instance

<br>

- ModelForm 의 instance 는 수정 대상이 되는 객체를 지정한다.

```python
[인스턴스 이름] = [모델 이름].objects.get(pk=pk)
[모델 폼 인스턴스 이름] = [모델 폼 이름](instance=[인스턴스 이름])
context = {
	"[모델 폼 인스턴스 이름]": [모델 폼 인스턴스 이름],
}
```

```html
{% csrf_token %}
{{ [모델 폼 인스턴스 이름].as_p }}
```

<br>

[위로가기](#목차)

<br>

## 9. Admin

<br>

- automatic admin interface

  - 장고에서는 관리자페이지를 자동으로 생성하는 기능이 있다.

  - 관리자 페이지

    - 모델 클래스를 `admin.py` 에 등록하고 관리

      ```python
      from django.contrib import admin
      from .models import [모델 이름]
      
      admin.site.register([모델 이름])
      ```

    - 레코드 생성 여부 확인에 매우 유용하며 직접 레코드를 기록 할 수도 있다.

  - admin 계정 생성

    - `python manage.py createsuperuser`
    - username 과 password 를 입력해 관리자 계정을 생성
      - email은 선택사항이기 때문에 입력하지 않고 enter를 입력해도 된다.

<br>

[위로가기](#목차)

<br>

## 10. Static files

<br>

- 웹 서버는 특정한 위치에 있는 자원을 요청받은 다음,

- 그것을 제공하는 응답을 처리하는 것이 기본 동작이다.

  - 어떤 URL 에 담겨있는 resource
    - HTTP request 로 요청
  - HTTP response 에 담아서 serving

- 웹 서버는 요청 받은 주소로 서버에 존재하는 static resource 를 제공

- static resource

  - 응답할 때 별도의 처리 없이 그대로 보여지는 파일
  - 이미지, Java script, CSS 같은 미리 준비된 추가 파일
  - 고정되어 있고 움직이지 않는 파일
  - 서비스 중에도 추가되거나 변경되지 않음
    - django 에서는 이러한 파일들을 static file 이라고 한다.
    - staticfiles 앱을 통해 정적 파일과 관련된 기능을 제공한다.

- 정적 파일 활용

  - `django.contrib.staticfiles` 가 `INSTALLED_APPS` 에 포함되어 있는지 확인

  - `settings.py` 에서 `STATIC_URL` 을 정의

    - `STATIC_URL`
      - `STATIC_ROOT` 에 있는 정적 파일을 참조할 때 사용할 URL
      - 개발 단계에서는 실제 정적 파일들이 저장되어 있는 `[앱]/static` 경로 외에도 `STATICFILES_DIRS` 에 정의된 추가 경로들을 탐색
      - 실제 경로나 파일이 아니다.
        - URL 만 존재
      - 비어있지 않은 값으로 설정한다면 반드시 `/` 로 끝나야 한다.
    - `STATIC_ROOT`
      - `collectstatic` 이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
        - django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로이다.
        - 직접 작성하지 않으면 django 프로젝트에서는 `settings.py` 에 작성되어있지 않다.
      - 개발 과정에서 `settings.py` 의 DEBUG 값이 True 로 설정되어 있으면 해당 값은 작용되지 않는다.
      - 실 서비스 환경에서 django 의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함이다.

  - 템플릿에서 static 태그를 사용하여 지정된 상대경로에 대한 URL 을 빌드

    ```html
    {% load static %}
    ...
    <img src="{% static '[static 하위 경로의 이름]/[사용할 이미지 이름]' %}"
    ```

  - `[앱 이름]/static/[앱 이름]/[사용할 파일]`

    - 앱의 static 디렉토리에 정적 파일 저장

  - `STATICFILES_DIRS`

    - 기본 경로인 `[앱]/static` 경로를 사용하는 것 외에 추가적인 정적 파일 경로를 정의하는 리스트

    - 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성

      ```python
      STATICFILES_DIRS = [
          BASE_DIR / 'static',
      ]
      ```

  - `STATIC_URL = "/static/"`
  - `STATIC_ROOT = BASE_DIR / "staticfiles"`
    - 루트 디렉토리 하위 `staticfiles` 디렉토리로 모든 정적 파일들이 모이게 된다.

<br>

[위로가기](#목차)

<br>

## 11. Django Auth

<br>

- django 에서 기본적으로 제공하는 장고 인증 시스템은 인증과 권한부여를 함께 처리

  - User
  - 권한 및 그룹
  - 암호 해시 시스템
  - Form 및 View 도구
  - 기타 적용가능한 시스템

- 필수 구성은 `settings.py` 의 `INSTALLEND_APPS` 에서 확인 가능

  - `django.contrib.auth`

- 사용하기 위한 사전 설정

  - accounts 앱 생성 및 등록

    ```python
    INSTALLED_APPS = [
        ['다른 앱 이름'],
    	'accounts',
        ...
    ]
    ```

    - **django 에서 auth 와 관련된 경로나 키워드들은 내부적으로 accounts 라는 이름으로 사용되고 있기 때문에 이름으로 accounts 가 권장됨**

  - url 분리 및 매핑

<br>

### 11-1. User model 활용하기

<br>

- Django 는 기본적인 인증 시스템과 여러 필드가 포함된 User model 을 제공한다.

- 대부분의 개발 환경에서 기본 User model 을 커스텀하여 사용한다.

  - Django 의 User model 은 기본적으로 username 을 식별 값으로 사용하는데 다른 것을 식별 값으로 사용하게 할 수 있다.

- User model 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate 를 실행하기 전에 마쳐야 한다.

- Django 은 `AUTH_USER_MODEL` 설정값으로 기본 유저모델을 재정의 할 수 있도록 함

  - `AUTH_USER_MODEL`

    - 프로젝트에서 User 를 나타낼 때 사용하는 모델
    - 마이그레이션 이후에는 변경할 수 없음
    - `AUTH_USER_MODEL` 가 참조하는 모델은 첫 번째 마이그레이션에서도 사용할 수 있어야 하기 때문에,
      - 첫 번째 마이그레이션에서 이미 확정이 되어있어야 한다.
      - 기본 값은 `AUTH_USER_MODEL = "auth.User"` 이다.
      - [원본 settings.py](https://github.com/django/django/blob/main/django/conf/global_settings.py)

  - 재정의 하는 방법

    - `AbstractUser` 를 상속받는 커스텀 User 클래스를 작성

    - 기존의 User 클래스도 `AbstractUser` 를 상속받기 때문에 커스텀 User 클래스도 똑같은 모습이다.

      ```python
      from django.contrib.auth.models import AbstractUser
      
      class User(AbstractUser):
      	pass
      ```

    - `settings.py` 에 `AUTH_USER_MODEL = "accounts.User"` 작성

    - `admin.py` 에 커스텀 User 모델을 등록

      ```python
      from django.contrib import admin
      from django.contrib.auth.admin import UserAdmin
      from .models import User
      
      admin.site.register(User, UserAdmin)
      ```

    - 변경이 완료된 후 DB를 열어보면 `auth_user` 테이블 대신 `accounts_user` 테이블을 사용하게 된다.

    - User 객체는 인증 시스템의 가장 기본

      - username
      - password
      - email
      - first_name
      - last_name

    - password 의 관리

      - Django 에서는 기본으로 PBKDF2 를 사용하여 저장한다.
      - 단방향 해시함수를 활용하여 비밀번호를 다이제스트로 암호화하며 복호화가 불가능함
      - 단방향 해시함수는 MD5, SHA-1, SHA-256 (django 에서 사용중) 등이 있다.
        - 단방향 해시함수의 경우 레인보우 공격 및 무차별 대입 공격 등의 문제가 발생할 수 있다.
        - 보완하기 위한 기법
          - 솔팅
            - 패스워드에 임의의 문자열을 추가하여 다이제스트를 생성
          - 키 스트레칭
            - 해시를 여러 번 반복하여 시간을 늘림

    - User 객체의 활용법

      - User 생성

      - User 비밀번호 변경

      - User 인증

        ```python
        user = User.objects.create_user(['유저 아이디'], ['유저 이메일'], ['비밀번호'])
        ###
        user = User.objects.get(pk=2)
        user.set_password(['새 비밀번호'])
        user.save()
        ###
        from django.contrib.auth import authenticate
        user = authenticate(username=['유저 아이디'], password=['비밀번호'])
        ```

<br>

### 11-2. 회원 가입

<br>

- 주어진 username 과 password 로 권한이 없는 새 user 를 생성하는 모델폼

- [세 개의 필드를 가짐](https://github.com/django/django/blob/stable/3.2.x/django/contrib/auth/forms.py#L75)

  - username
  - password1
  - password2

- 회원 가입 로직을 작성하기 위해 사용되는 UserCreationForm 에는 커스텀 유저 모델을 상속시켜줘야 한다.

  ```python
  from django.contrib.auth import get_user_model
  from django.contrib.auth.forms import UserCreationForm
  
  class CustomUserCreationForm(UserCreationForm):
  	class Meta(UserCreationForm.Meta):
  		model = get_user_model()
  ```

- `get_user_model()`

  - 현재 프로젝트에서 활성화된 사용자 모델을 반환
  - Django 에서는 User 클래스는 커스텀을 통해 변경 가능하다.
    - 직접 참조하는 대신 `get_user_model()` 을 사용할 것을 권장한다.

<br>

[위로가기](#목차)

<br>
