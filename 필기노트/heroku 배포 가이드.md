# 가이드

<br>

## 목차

<br>

[1. 헤로쿠 배포 전 준비사항](#1-헤로쿠-배포-전-준비사항)

[2. 헤로쿠 배포](#2-헤로쿠-배포)

[3. 에러 모음집](#3-에러-모음집)

<br>

## 1. 헤로쿠 배포 전 준비사항

<br>

- 가상환경 생성 후 로컬에서 페이지 정상 작동 확인까지 모두 마쳤다는 것을 전제로 한다.

---

- Static 파일 모아주기.

  - heroku 는 스태틱 파일들을 한 곳에서  모아서 넘겨줘야 잘 작동한다.

  - 경로를 설정해줘야 한다.

  - `settings.py` 에 아래의 코드를 입력한다.

    ```python
    STATIC_URL = "/static/"
    STATIC_DIR = os.path.join(BASE_DIR, "static")
    
    STATICFILES_DIRS = [
        STATIC_DIR,
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
    ```

  - 프로젝트 루트 경로 바로 아래에 static_root 라는 경로를 만들어주고 거기에서 static 파일들을 관리 할 것이다.

  - `python manage.py collectstatic` 으로 정적 파일들을 한 곳에 모은다.

---

- 시크릿 키 분리하기

  - Django 에서 사용되는 인증키

  - 숨겨져야 한다.

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
       - 까먹지 말고 `import os` 해주기

    4. `.gitignore` 에 `secrets.json` 을 등록한다.

---

- `settings.py` 의 `DEBUG = True` 로 되어있는 것을 `DEBUG = False` 로 바꿔놓는다.

  - 디버그 모드는 오류가 났을 때 너무 친절하게 알려주기 때문에 나쁜 사람들에게 그 정보가 넘어가면 안좋은 결과를 초래할 수 있다.
  - 그러한 디버그 모드를 꺼주는 변수임

- `settings.py` 에서 `ALLOWED_HOSTS` 에 `"*"` 을 넣어준다.

  ```python
  ALLOWED_HOSTS = [
      "*",
  ]
  ```

- `Procfile` 이라는 파일을 작성한다.

  - `web: gunicorn [프로젝트 이름].wsgi --log-file -  `

- `runtime.txt` 이라는 파일을 작성한다.

  - 자기 파이썬 버전을 적는다.
  - `python-3.10.7`

- `pip install gunicorn whitenoise dj-database-url psycopg2-binary` 를 입력하여 설치한다.

- `settings.py` 의 `MIDDLEWARE` 두 번째 위치에 `"whitenoise.middleware.WhiteNoiseMiddleware"` 를 추가한다.

  ```python
  MIDDLEWARE = [
      ...
      "whitenoise.middleware.WhiteNoiseMiddleware", # 두 번째 위치
      ...
  ]
  ```

- `settings.py` 의 제일 밑에 다음 코드를 추가한다.

  ```python
  import dj_database_url
  db_from_env = dj_database_url.config(conn_max_age=500)
  DATABASES['default'].update(db_from_env)
  ```

- 배포 전에 `pip freeze > requirements.txt` 로 받은 것들 적어두기

- 만약 다른 `.git` 으로 이미 깃에서 관리되고 있다면 다른 곳으로 복붙 한다음에 `.git` 을 없애야 된다.

- heroku 가입하기

<br>

[위로 가기](#목차)

<br>

## 2. 헤로쿠 배포

<br>

1. `git init`
2. `git add .`
3. `git commit -m "init"`
4. `heroku login`
   - 그 다음 아무 키나 누르면 잠깐 멈췄다가 로그인 하라고 새 창이 뜬다.
   - 클릭하면 창이 바뀌면서 로그인이 된다.
5. `heroku create`
   - 이미 배포를 했고 업데이트 하려는 경우에는 여러번 create 할 필요는 없다.
     - 1~3 까지 진행하고 6~7 과정만 진행하면 된다.
6. ` git push heroku master`
   - 기존에 서비스 되고 있던 페이지의 DB 는 다 초기화 되기 때문에 업데이트 하는 경우에는 미리 백업하고 진행해야 한다.
   - [에러](#3-에러-모음집)가 나면 `git push heroku HEAD:master` 를 하라는데 난 잘 모르겠다.
   - 경험적으로는 그냥 밑에 모아놓은 [에러 모음집](#3-에러-모음집)에서 [에러](#3-에러-모음집)를 해결해서 진행하는 것이 더 나았다...
7. `heroku run python manage.py migrate`
8. `heroku run python manage.py createsuperuser`
9. `heroku open`

<br>

[위로 가기](#목차)

<br>

## 3. 에러 모음집

<br>

1. `git push heroku master` 할 때 로그에 `heroku config:set DISABLE_COLLECTSTATIC=1` 가 있다면 콘솔에 `heroku config:set DISABLE_COLLECTSTATIC=1` 를 그대로 친 다음 푸시하면 잘 된다.
2. css 파일이 잘 안나온다면 경로 설정이 잘 되어있는지 봐야 된다.
   - css 경로 설정은 프로젝트 맨 위,
   - 즉 만들때 `django-admin startproject [프로젝트 이름] .` 으로 했으니,
   - `.` 의 위치에 `STATIC_ROOT` 를 만들고 거기로 `python manage.py collectstatic` 해 주면 된다.
3. 깃 배쉬에서 로그인이 안 될 때가 있는데 vscode 로 하면 잘 될 수도 있다.
4. 미디어 파일은 현재까지 우리가 배운 지식수준 (10월 16일 기준) 으로는 안 되는게 정상인 것 같다.
   - 이미지파일을 올리려면 static 을 통해서 넣으면 잘 된다.
5. `git push heroku master` 할 때 자꾸 `rejected` 가 될 때, 로그에 `Building wheel for twisted-iocpsupport (pyproject.toml) did not run successfully` 라는 기록이 있으면 `requirements.txt` 에서 `twisted-iocpsupport` 랑 `twist` 들어간 모듈 두 개를 `requirements.txt` 에서 지우고 하면 된다.
6. `heroku run python manage.py migrate` 가 안된다면 깃 이그노어에 `.sqlite3` 를 제외하면 된다.
7. `heroku run python manage.py createsuperuser` 로 운영자 계정을 만들었는데 정작 배포된 사이트의 /admin 에서 해당 계정으로 안 들어가지면 로컬에서 `python manage.py createsuperuser` 로 admin 계정을 만든 다음 heroku 로 마이그레이트 하고 들어가면 되는 경우가 있다.
8. `runtime.txt` 에 파이썬의 버전을 적을 때 대문자가 아니고 소문자이다.
   - `python --version` 하면 `Python X.X.X` 와 같이 **대문자로 결과가 출력되는데 그대로 복붙하면 버전이 안 맞는다고 할 수가 있다.**
   - 반드시 소문자로 `python-X.X.X` 를 적는다.
   - 그런데도 안 된다면 버전 호환 문제일 수 있기 때문에 heroku 공식 문서에서 호환되는 버전을 찾아서 설치한다.

<br>

[위로 가기](#목차)

<br>

---

###### 여태 만들었던 페이지들

- [할 일 메모장](https://boiling-temple-99523.herokuapp.com/)
- [영화 리뷰 팀 프로젝트](https://lit-scrubland-98413.herokuapp.com/reviews/index/)

---

<br>
