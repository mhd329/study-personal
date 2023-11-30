# Django guidebook

<br>

## 목차

<br>

[1. 파이썬 가상환경](#1-파이썬-가상환경)

> [1-1. 가상환경 생성](#1-1-가상환경-생성)
>
> [1-2. 가상환경 실행](#1-2-가상환경-실행)
>
> [1-3. 가상환경 삭제](#1-3-가상환경-삭제)

[2. Django LTS](#2-Django-LTS)

>[2-1. Django LTS 설치](#2-1-Django-LTS-설치)
>
>[2-2. Django 프로젝트 생성](#2-2-Django-프로젝트-생성)
>
>[2-3. Django 실행](#2-3-Django-실행)

<br>

## 1. 파이썬 가상환경

<br>

- 파이썬 가상환경이란?
  - 자신이 원하는 파이썬 환경 하에서 작업을 하기 위해 해당 작업에 필요한 python 모듈만을 모아 놓은 환경이다.
  - 가상 환경은 독립적으로 관리가 된다.
    - 독립적으로 관리되고 있기 때문에 원인 미상의 오류를 방지할 수 있다.
    - 해당 환경 내에서 어떤 사고가 발생하더라도 피해를 최소화 할 수 있다.

<br>

### 1-1. 가상환경 생성

<br>

- windows 기준
  1. 가상환경을 만들기 원하는 경로로 간다.
  2. git bash 의 `mkdir` 로 가상환경의 루트 디렉토리를 만든다.
  3. 라트 디렉토리로 들어온 다음 git bash 에서 `python -m venv [가상환경 이름]` 으로 가상환경 폴더를 만든다.
  4. `ls`  명령어로 만들어졌는지 확인한다.

<br>

### 1-2. 가상환경 실행

<br>

1. activate 파일이 있는 곳에서 해당 파일을 실행시켜야 한다.
2. `source [activate 파일 까지의 경로]`
   - ``source ./[가상환경 이름]/Scripts/activate`
3. 가상환경 해제는 가상환경을 실행중인 상태에서 git bash 에 `deactive` 를 입력하면 가상환경이 해제된다.

<br>

- 가상환경 생성 후 가상환경 폴더를 다른 곳으로 이동시켰다면,
  - activate.bat
  - Activate.ps1
  - activate
    - 세 파일 안의 VIRTUAL_ENV 부분을 이동시킨 경로로 수정해주어야 한다.

<br>

### 1-3. 가상환경 삭제

<br>

- python venv 의 경우는 그냥 디렉토리 자체를 지우면 된다.
  - `rm -r [가상환경 폴더 이름]`

<br>

## 2. Django LTS

<br>

- Django LTS 란?
  - LTS
    - Long-Term Support releases
    - 장기지원 되는 버전
    - 일반적으로 3년 정도 지원한다.
  - 현재까지 Django LTS 버전 중 가장 안정적인 최신 버전은 Django 3.2 버전이다.

<br>

### 2-1. Django LTS 설치

<br>

1. 가상환경의 루트 경로에서 가상환경을 실행시킨다.
2. `pip install Django==[설치를 원하는 버전]`
   - `pip install Django==3.2.12`
3. `pip list` 명령어로 잘 설치되었는지 확인한다.

<br>

### 2-2. Django 프로젝트 생성

<br>

1. `django-admin startproject [프로젝트 이름] [시작할 경로]`
2. `ls` 명령어로 현재 루트 경로의 하위에 잘 설치되었는지 확인한다.
   - manage.py 파일과 프로젝트의 이름으로 된 디렉토리가 있어야 한다.
   - 시작할 경로가 정해지지 않은 경우 자동으로 루트 경로 하위에 프로젝트 이름으로 새로운 경로가 추가된다.
     - manage.py 파일은 그 경로 하위에 생성되기 때문에 Django 를 실행하려는 경우 그 경로까지 이동해아 한다.
3. `django-admin startapp [앱 이름]` 혹은 `python manage.py startapp [앱 이름]`

<br>

### 2-3. Django 실행

<br>

1. `python manage.py runserver`
2. 웹 브라우저의 주소창에 http://localhost:8000/ 를 입력한다.
3. Django 로켓이 발사되어있는 이미지를 확인한다.
4. git bash 에서 Ctrl + C 를 눌러 서버를 종료시킬 수 있다.

<br>

[목차로 가기](#목차)

<br>

