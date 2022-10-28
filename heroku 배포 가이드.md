





<br>

[목차로 바로 가기](#목차)

<br>

## Heroku deployment guide v0.2.2

<br>

- 내용 수정
  - 스태틱, 미디어 루트 경로 간소화
  - 1-4. 항목에서 db관련 설명 추가

<br>

## Heroku deployment guide v0.2.1

<br>

- 내용 수정
  - 좀 더 자세하게 씀
    - ALLOWED_HOSTS
    - 추가 보안 설정
    - 헤로쿠 배포 관련 설정

<br>

# Heroku deployment guide v0.2.0

<br>

- 재분류
  - 파트에 맞게 항목들 재분류
  - 목차 재분류
    - 배포 이전, 이후로 분류
- 추가
  - 미디어 파일 관련 설정 항목
  - 보안관련 설정 항목
  - 이슈 관련 내용 추가
    - 미디어 파일 관련 이슈 해결
    - db 관련 이슈 해결

<br>

## 목차

<br>

[1. 헤로쿠 배포 전 준비사항](#1-헤로쿠-배포-전-준비사항)

> [1-1. 정적, 미디어 파일 관련](#1-1-정적-미디어-파일-관련)
>
> [1-2. 보안 관련 설정](#1-2-보안-관련-설정)
>
> [1-3. 추가 보안 설정 ( 선택사항 )](#1-3-추가-보안-설정--선택사항-)
>
> > [각 항목에 대한 설명들](#각-항목에-대한-설명들)
>
> [1-4. 헤로쿠 배포 관련 설정](#1-4-헤로쿠-배포-관련-설정)

[2. 헤로쿠 배포](#2-헤로쿠-배포)

[3. 이슈 모음집](#3-이슈-모음집)

> [3-1. 배포 이전 이슈들](#3-1-배포-이전-이슈들)
>
> [3-2. 배포 이후 웹 운영 이슈들](#3-2-배포-이후-웹-운영-이슈들)

<br>

## 1. 헤로쿠 배포 전 준비사항

<br>

### 1-1. 정적, 미디어 파일 관련

<br>

- static, media 파일 경로 설정

  - heroku 는 스태틱 파일들을 한 곳에 모아서 넘겨줘야 잘 작동한다.

  - static 파일 관련

    - `settings.py` 에 아래의 코드를 입력한다.
    - 
        ```python
        STATIC_URL = "/static/"
        STATIC_ROOT = BASE_DIR / "staticfiles"
        ```
        
    - 프로젝트 루트 경로 ( `settings.py` 가 있는 폴더 ( 프로젝트 이름으로 된 폴더 ) 가 들어있는 곳 ) 에 static_root 라는 경로를 만들어주고 거기에서 static 파일들을 관리 할 것이다.
    
  - media 파일 관련 ( 미디어 파일이 안 올라간다면 아래의 과정에서 빠진 것이 있는지 점검해보세요~!! )
  
    - `Pillow` 를 설치해준다.
      - `pip install Pillow`
  
    - `imagekit` 을 설치해준다.
      - `pip install django-imagekit`

    - `"imagekit"` 을 `INSTALLED_APPS` 에 추가해준다.
      - 미디어 파일들도 한 곳에 모아놓고 관리해야 한다.

    - `settings.py` 에 아래의 코드를 입력한다.
    - 
      ```python
      MEDIA_URL = "/media/"
      MEDIA_ROOT = BASE_DIR / "mediafiles"
      ```
      
    - 프로젝트 루트 경로 ( `settings.py` 가 있는 폴더 ( 프로젝트 이름으로 된 폴더 ) 가 들어있는 곳 ) 에 media_root 라는 경로를 만들어주고 거기에서 media 파일들을 관리 할 것이다.
    
    - `urls.py` 에서 미디어 파일 경로 추가해주기
    
    - `urlpatterns` 밖에 경로를 추가해준다.
    
      ```python
      urlpatterns = [
          ...
      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
      ```
    
    - `models.py` 에 문제가 없는지 점검한다.
    
    - `views.py` 의 미디어 파일을 사용하려는 함수에 `request.FILES` 가 잘 있는지 점검한다.
    
    - `templates` 폴더에서 미디어 파일을 사용려는 `html` 템플릿에 `enctype="multipart/form-data"` 가 잘 있는지 점검한다.
  
- WhiteNoise 설치

  - 배포 전에 `DEBUG = False` 로 해야한다.
  - 그런데 그렇게 되면 기존에 쓰던 정적 파일들의 경로를 장고가 못 찾게 된다.
  - WhiteNoise 를 사용하여 해결 할 수 있다.
    - `pip install whitenoise` 로 화이트노이즈를 설치한다.
    - `settings.py` 의 `MIDDLEWARE` 두 번째 위치에 `"whitenoise.middleware.WhiteNoiseMiddleware"` 를 추가한다.

      ```python
      MIDDLEWARE = [
          ...
          "whitenoise.middleware.WhiteNoiseMiddleware", # 두 번째 위치
          ...
      ]
      ```

- 모든 설정이 끝났다면 `python manage.py collectstatic` 으로 정적 파일들을 한 곳에 모은다.

<br>

[위로 가기](#목차)

<br>

### 1-2. 보안 관련 설정

<br>

- **중요 : 시크릿 키 분리하기** ( 했다면 생략 )

  - 이 문서에서 설명하는 방법 말고도 [헤로쿠에서 직접 관리하는 방법](https://www.securecoding.com/blog/how-to-securely-deploy-django-to-heroku/#Setup_Heroku) 이 있다.

    - 나는 아래의 방법이 더 편해서 그냥 했다.

  - **Django 에서 사용되는 인증키는 반드시 숨겨져야 한다.**

  - 순서

    1. 프로젝트 루트 폴더에 secrets.json 파일을 만든다.

       ```json
       {
           "SECERT_KEY": "[내 장고 시크릿 키]"
       }
       ```

    2. 프로젝트의 `settings.py` 에 들어간다.

    3. `SECRET_KEY` 에 원래 있던 시크릿 키 대신 `os.path.join(BASE_DIR, "secrets.json")` 를 넣는다.

       - `SECRET_KEY = os.path.join(BASE_DIR, "secrets.json")`

    4. **`.gitignore` 에 `secrets.json` 을 등록한다.**

- `settings.py` 의 `DEBUG = True` 로 되어있는 것을 `DEBUG = False` 로 바꿔놓는다.

  - 디버그 모드는 오류가 났을 때 너무 친절하게 알려주기 때문에 나쁜 사람들에게 그 정보가 넘어가면 안좋은 결과를 초래할 수 있다.
  - 그러한 디버그 모드를 꺼주는 작업임

- `ALLOWED_HOSTS` 에 아래 설정을 입력한다.

  ```python
  ALLOWED_HOSTS = [
      "localhost",
      "127.0.0.1",
      ".herokuapp.com",
  ]
  ```
  
  - 이것은 Host 헤더를 확인하는 작업이다.

  - 접근 가능 도메인을 지정해서 관리하는 것이다.

  - `*` 은 모든 도메인을 허용하는 것이다.
    - **오류가 나는 경우 `ALLOWED_HOSTS` 에 `"*"` 을 넣어준다.**
  

<br>

[위로 가기](#목차)

<br>

#### 1-3. 추가 보안 설정 ( 선택사항 )

- 참고하여 만들었음 : [django 기본 보안 설정](https://blog.jun2.org/development/2019/07/23/django-security-options.html)
- 뭔 소리인지 잘 모르겠지만 유용할것 같아서 가져왔다 !
  - 선택사항이기 때문에 안 써도 잘 작동함
  - 복붙해봤기 때문에 저를 따라서 복붙할 시 작동을 보장할 수 없습니다...
  - 그렇기 때문에 복붙해서 문제가 생길 경우 한꺼번에 지우기 쉽게 한 곳에 모아서 붙여넣으세요.
    - MIDDLEWARE 부분은 원본을 안까먹게 잘 기억하세요.


<br>

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ALLOWED_HOSTS = ['위에서 적었던 것들']

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_HSTS_SECONDS = 31536000  # 365 * 24 * 60 * 60
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

CSP_DEFAULT_SRC = ("'self'")

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = ['내 Heroku app 주소'] => 주소 끝나는 곳에 '/' 를 빼세요 !!
CORS_URLS_REGEX = r'^/api/.*$'

CORS_ALLOW_CREDENTIALS = True 

CSRF_TRUSTED_ORIGINS = CORS_ORIGIN_WHITELIST

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'
```

<br>

[위로 가기](#목차)

<br>

#### 각 항목에 대한 설명들

<br>

- SSL/HTTPS

    ```python
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    ```

    - HTTP 로 요청이 들어오면 HTTPS 로 리다이렉트 해준다.

- HSTS

  ```python
  SECURE_HSTS_SECONDS = 31536000  # 365 * 24 * 60 * 60
  SECURE_HSTS_PRELOAD = True
  SECURE_HSTS_INCLUDE_SUBDOMAINS = True
  ```

  - HTTPS 연결이 아닌 경우에 차단한다.
  - `SECURE_HSTS_SECONDS` 의 시간을 60초 정도로 작게 해서 테스트를 하고 서서히 늘려가면 좋다.
  - 개발 환경에서는 인증서 문제가 있을 수 있기 때문에 개발 편의상 프로덕션 환경에만 적용하는것이 좋다.

- X-Content-Type-Options

    ```python
    SECURE_CONTENT_TYPE_NOSNIFF = True
    ```

    - `X-Content-Type-Options: nosniff` 헤더를 응답한다.
    - MIME type을 브라우저가 추측하지 말고 지정한 형식으로만 파일을 사용하도록 한다.

- X-XSS-Proection

    ```python
    SECURE_BROWSER_XSS_FILTER = True
    ```

    - `x-xss-protection: 1; mode=block` 헤더를 응답한다.
    - 브라우저에서 XSS 보호기능을 활성화 한다.
    - XSS 공격이 감지되면 화면을 빈 페이지로 그린다.

- X-Frame-Options

    ```python
    `X_FRAME_OPTIONS = 'DENY'
    ```

    - `X-Frame-Options: deny` 헤더를 응답한다.
    - 기본값은 `SAME_ORIGIN` 인데 `DENY` 로 하고 필요한 Endpoint만 `@xframe_options_sameorigin` 데코레이터를 통해 지원하는 것이 좋다.

- CSRF

    ```python
    SESSION_COOKIE_HTTPONLY = True
    CSRF_COOKIE_HTTPONLY = True
    ```

    - HttpOnly 기본값이 True 이기 때문에 세팅하지 않아도 된다.
    - 설정을 하면 JS 에서 쿠키에 접근하지 못한다.

    ```python
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    ```

    - Secure를 설정하면 HTTPS 프로토콜에서만 브라우저가 서버로 쿠키를 포함해서 요청한다.

    ```python
    SESSION_COOKIE_SAMESITE = 'Lax'
    CSRF_COOKIE_SAMESITE = 'Lax'
    ```

    - 기본값이 `Lax`이기 때문에 세팅하지 않아도 된다.

- CORS

    - django-cors-headers 라이브러리를 사용한다.

    ```python
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ORIGIN_WHITELIST = ['https://sub.example.com']
    CORS_URLS_REGEX = r'^/api/.*$'
    
    CORS_ALLOW_CREDENTIALS = True 
    
    CSRF_TRUSTED_ORIGINS = CORS_ORIGIN_WHITELIST
    ```

    - 원문 설명이 길어서 해당 링크에서 CORS 항목을 참고하세요.

- CSP

    - django-csp 라이브러리를 사용한다.

    ```python
    CSP_DEFAULT_SRC = ("'self'")
    ```

    - 가능한 조합이 매우 많다.
    - `CSP_DEFAULT_SRC = ("'self'")` 으로 설정하고 하나씩 정책을 변경해 가면서 적용하면 좋다.

<br>

[위로 가기](#목차)

<br>

### 1-4. 헤로쿠 배포 관련 설정

<br>

- 일단 heroku 가입하기

- 그 다음 루트 경로에 `Procfile` 이라는 파일을 작성한다.
  - `web: gunicorn [프로젝트 이름].wsgi --log-file -  `

- 루트 경로에 `runtime.txt` 이라는 파일을 작성한다.
  - 자기 파이썬 버전을 적는다.
  - `python-3.10.7`

- `pip install gunicorn dj-database-url psycopg2-binary` 를 입력하여 설치한다.

  - 헤로쿠에서 db는 postgreSQL 에서 관리하게 된다.

  - `psycopg2` 와 `dj-database-url` 는 postgreSQL 관련 모듈인데 자세히는 잘 모르겠다.
    - ( 2022. 10. 26 ) 파이썬 3.11 에서는 잘 안되는 이슈가 있다.

- `settings.py` 의 `DATABASES` 아래에 다음 코드를 추가한다.

    ```python
    import dj_database_url
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
    ```

- 배포 전에 `pip freeze > requirements.txt` 로 받은 것들 적어두기


<br>

## 2. 헤로쿠 배포

<br>

- 기존에 쓰던 git 저장소가 없는 경우

1. `git init`
2. `git add .`
3. `git commit -m "init"`
4. `git push origin master`

- 기존 git 저장소에서 관리하여 이미 `.git` 폴더가 있는 경우 위의 1~4 과정은 생략하고 아래부터 시작한다.

1. `heroku login`
   - 그 다음 아무 키나 누르면 잠깐 멈췄다가 로그인 하라고 새 창이 뜬다.
   - 클릭하면 창이 바뀌면서 로그인이 된다.
2. `heroku create`
   - 이미 배포를 했고 업데이트 하려는 경우에는 여러번 create 할 필요는 없다.
     - 그러한 경우 1\~3 까지 진행하고 6\~7 과정만 진행하면 된다.
3. ` git push heroku master`
   - [에러](#3-에러-모음집)가 나면 `git push heroku HEAD:master` 를 하라는데 써본적이 없어서 잘 모르겠다...
4. `heroku run python manage.py migrate`
5. `heroku run python manage.py createsuperuser`
6. `heroku open`
   - 잘 된다면 페이지 배포가 완료된 것이다 !

<br>

[위로 가기](#목차)

<br>

## 3. 이슈 모음집

<br>

### 3-1. 배포 이전 이슈들

<br>

1. 깃 배쉬에서 로그인이 먹통일 때가 있는데 vscode 로 하면 잘 될 수도 있다.
   - 로그인 하라고 뜨고 아무 키나 눌렀을 때 바로 페이지가 떠야 함
2. `git push heroku master` 할 때 로그에 `heroku config:set DISABLE_COLLECTSTATIC=1` 가 있다면 콘솔에 `heroku config:set DISABLE_COLLECTSTATIC=1` 를 그대로 친 다음 푸시하면 잘 된다.
   - 아마 가장 자주 발생하는 에러일것 같다.
3. `git push heroku master` 할 때 자꾸 `rejected` 가 되는데, 로그에 `Building wheel for twisted-iocpsupport (pyproject.toml) did not run successfully` 라는 기록이 있는 경우
   - pip list 에 `twisted-iocpsupport` 이라는 모듈이 설치되어 있어서 발생하는 오류이다.
     - 이것이 무엇인지 대충 찾아보았는데 문제가 발생하는 이유를 [스택 오버플로우](https://stackoverflow.com/questions/67218268/issue-deploying-django-app-onto-heroku-due-to-twisted-iocpsupport)에서 찾아보았다.
       - `twisted-iocpsupport` 는 Windows 전용 플랫폼 모듈이다.
       - Heroku 는 리눅스 기반 플랫폼이다.
   - `pip uninstall twisted-iocpsupport` 하기
   - `requirements.txt` 에서 `twisted-iocpsupport` 를 지우고 다시 `requirements.txt` 를 만들기
4. `heroku run python manage.py migrate` 가 안된다면 `.gitignore` 에서 `.sqlite3` 를 제외하면 된다.
   - Heroku 로 마이그레이트 해줘야 하기 때문에 무시를 잠깐 풀어줘야 한다.
5. `heroku run python manage.py createsuperuser` 로 운영자 계정을 만들었는데 정작 배포된 사이트의 /admin 에서 해당 계정으로 안 들어가지는 경우
   - 로컬에서 먼저 `python manage.py createsuperuser` 로 admin 계정을 만든 다음 다시 heroku 로 마이그레이트 하고 들어가면 되는 경우가 있다.
6. 로그에 버전 관련하여 문제가 있는 경우

   - `runtime.txt` 에 파이썬의 버전을 적을 때 혹시 대문자로 적혀있는지 확인한다.

   - `python --version` 하면 `Python X.X.X` 와 같이 대문자로 결과가 출력되는데 그대로 복붙하면 버전이 안 맞는다고 할 수가 있다.

     - 소문자로 `python-X.X.X` 를 적는다.

     - 그런데도 안 된다면 버전 호환 문제일 수 있기 때문에 heroku 공식 문서에서 호환되는 버전을 찾아서 설치한다.

<br>

### 3-2. 배포 이후 웹 운영 이슈들

<br>

1. css 파일이 잘 안나오는 경우
   - `settings.py` 경로 설정이 잘 되어있는지 봐야 된다.

2. 미디어 파일이 안나오는 경우
   - amazon S3 를 사용하기
     - 조건부 유료 서비스이긴 한데 우리의 사용량으로는 괜찮을 것 같다...
     - 내 사용량으로는 문제없을 것 같아서 그냥 썼다.
       - **반드시 비용에 대해서 별도로 확인해보시기 바랍니다.**
       - **만약 사용한다면 키 관리를 철저히 해야 함 !!**
     - 사용법
       - [버킷 만들기](https://integer-ji.tistory.com/12)
       - [heroku 에 aws s3 연결하기](https://integer-ji.tistory.com/13)

3. 웹에 올려놓은 글 같은 것들이 자꾸 사라짐

   - Heroku [dynos](https://www.heroku.com/dynos) 라는 컨테이너 관리 기능은 컨테이너를 일정 주기로 초기화시킨다.

   - 무료 버전 heroku는 30분 동안 변동이 없으면 sleep 모드로 들어가면서 파일들을 삭제시킨다.
   - 유료 버전 heroku 는 매일 다시 시작된다.
   - 그렇기 때문에 웹 상에 여러 게시글을 올려도 일정 시간이 지나면 초기화된다.
     - 자료 참고 : [헤로쿠 파일이 삭제되는 이유](https://help.heroku.com/K1PPS2WM/why-are-my-file-uploads-missing-deleted-from-the-application)
   - 해결책
     - 별도 애드온을 추가
     - PostgreSQL 연결하여 보존
       - Windows 10 에서 확인된 방법 : [Heroku+Postgres(hobby) 무료 호스팅+DB 사용 설정](https://m.blog.naver.com/batgirl1/222126972818)

<br>

[위로 가기](#목차)

<br>

---

###### 여태 만들었던 페이지들

- [할 일 메모장](https://boiling-temple-99523.herokuapp.com/)
- [영화 리뷰 팀 프로젝트](https://lit-scrubland-98413.herokuapp.com/)
- [영화 리뷰 팀 프로젝트 2](http://guarded-tundra-99188.herokuapp.com/)

---

<div align="center">
	<h6>
    	최종 수정일 2022 10 26
    </h6>
</div>