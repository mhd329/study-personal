# Database

<br>

## 목차

<br>

[1. 관계형 데이터베이스](#1-관계형-데이터베이스)

[2. SQLite](#2-SQLite)

[3. SQL](#3-SQL)

[4. Hello World !](#4-Hello-World-!)

[5. CRUD](#5-CRUD)

> [5-1. Create](#5-1-Create)

> [5-2. Read](#5-2-Read)

> > [5-2-1. SELECT](#5-2-1-SELECT)

> >[5-2-2. WHERE](#5-2-2-WHERE)

> > [5-2-3. SQLite 집계 함수](#5-2-3-SQLite 집계 함수)

> >[5-2-4. LIKE](#5-2-4-LIKE)

> > [5-2-5. ORDER BY](#5-2-5-ORDER BY)

> > [5-2-6. 기본 함수와 연산](#5-2-6-기본 함수와 연산)

> [5-2-7. GROUP BY](#5-2-7-GROUP BY)

> [5-3. Update](#5-3-Update)

[6. CASE](#6-CASE)

[7. 서브쿼리](#7-서브쿼리)

[8. JOIN](#8-JOIN)

[9. 모델링](#9-모델링)

[파이썬-DB 1. ORM](#파이썬-DB-1-ORM)

[파이썬-DB 2. QuerySet API](#파이썬-DB-2-QuerySet-API)

[파이썬-DB 3. ORM 확장](#파이썬-DB-3-ORM 확장)

<br>

## 1. 관계형 데이터베이스

<br>

- RDB
  - 관계형 데이터베이스
  - keys, values 간의 관계를 table 로 정리한 것
- schema
  - 자료의 구조, 표현 방법, 관계등의 표현 방식에 대한 약속의 집합
  - 데이터 베이스 안에 테이블들이 들어가고 그 테이블에 대한 일종의 생성 규칙
- table
  - 열(field) 과 행(record) 의 모습으로 표현되어지는 데이터들의 집합
  - column
    - 각각의 열에 교유한 데이터 형식을 지정
    - 데이터들이 각 열을 바탕으로 분류되어 들어감
  - row
    - 하나의 정보집합을 구성하는 각각의 데이터들이 열의 구분단위에 따라 분류되어진 상태로 속해있음
- Primary Key
  - 각 record 의 고유 값
  - db 관리 및 관계 설정시 주요하게 활용됨

<br>

[목차로 가기](#목차)

<br>

## 2. SQLite

<br>

- Data Type
  1. Null
  2. INTEGER
     - 8 바이트에 저장된 부호 있는 정수
  3. REAL
     - 8 바이트에 저장된 부동 소수점
  4. TEXT
  5. BLOB
     - 입력된 그대로 정확하게 저장된 데이터
     - 별다른 타입이 없음
- 권장 타입
  - INTEGER
  - TEXT
  - BLOB
  - REAL
  - NUMERIC

<br>

[목차로 가기](#목차)

<br>

## 3. SQL

<br>

- Keywords
  - INSERT
  - SELECT
  - UPDATE
  - DELETE

<br>

[목차로 가기](#목차)

<br>

## 4. Hello World !

<br>

- DB 생성

  - ```sql
    .database
    ```

- CSV file to table

  - ```sql
    .import 파일 이름.csv 테이블 이름
    ```

  - ```sql
    .mode csv
    .import hellodb.csv examples
    .table
    >>> examples
    ```

- 조회

  - ```sql
    .tables
    ```

  - 모든 테이블의 이름 출력

  - ```sql
    SELECT * FROM examples;
    ```

  - 특정 테이블의 레코드 정보를 반환

  - ```sql
    SELECT 연산 AS 연산된 값을 표시할 이름
    ```

  - 위와 같이 쓰면 복잡한 연산식을 계산하고 출력할 때 필드의 형태로 연산식의 이름을 정해줄 수 있다.

- terminal view switching

  - ```sql
    .headers on
    .mode column
    ```

- 테이블 생성 및 삭제

  - ```sql
    CREATE TABLE 테이블이름 (
        id INTEGER
        name TEXT
    );
    ```

  - ```sql
    DROP TABLE 테이블이름;
    ```

  - ```sql
    .tables
    ```

  - 위 명령어로 테이블 확인 가능

  - ```sql
    .schema 테이블이름
    ```

  - 테이블의 schema 조회

- 필드 제약 조건
  - NOT NULL
    - NULL VALUE 입력금지
  - UNIQUE
    - 중복되는 VALUE 입력 금지
    - NULL VALUE 는 중복 가능
  - PRIMARY KEY
    - TABLE 에서 반드시 하나
    - NOT NULL + UNIQUE
  - FOREIGN KEY
    - 외래키
    - 다른 TABLE Key
  - CHECK
    - 조건으로 설정된 값만 입력 허용
  - DEFAULT
    - 기본 설정 값

<br>

[목차로 가기](#목차)

<br>

## 5. CRUD

<br>

### 5-1. Create

- INSERT

  - 테이블에 단일 행 삽입

  - ```sql
    INSERT INTO 테이블이름 (컬럼1, 컬럼2) VALUES (값1, 값2)
    ```

  - 테이블에 정의된 모든 열에 맞춰 순서대로 입력

  - ```sql
    INSERT INTO 테이블이름 VALUES (값1, 값2, 값3);
    ```

- rowid
  - sqlite 에서 테이블 생성시 schema 에 id 를 따로 작성하지 않은 경우, insert 마다 하나씩 증가하며 자동으로 입력되는 pk 컬럼
  - schema 에 id 를 직접 작성하는 경우, insert 할 때 입력할 column 을 명시하지 않으면 자동으로 입력되지 않음
  - value 에 id를 포함하거나 각 value 에 맞는 column 을 명시적으로 작성해야 한다.

<br>

[목차로 가기](#목차)

<br>

### 5-2. Read

<br>

#### 5-2-1. SELECT

<br>

- 테이블에서 데이터 조회
- 다양한 절(clause) 과 함께 사용
- SELECT +
  - ORDER BY
  - DISTINCT
  - WHERE
  - LIMIT +
  - OFFSET
  - GROUP BY

<br>

[목차로 가기](#목차)

<br>

#### 5-2-2. WHERE

<br>

- 특정 조건으로 데이터 조회
- if 문
- WHERE +
  - 비교 연산자
    - == 대신 = 를 쓰는것을 제외하고는 다 똑같음
  - AND
  - OR
  - NOT
  - 연산자 우선순위를 소괄호를 이용해 적절하게 제어해야 한다.
- BETWEEN
  - WHERE 필드이름 BETWEEN 값1 AND 값2
    - 값끼리 비교
- IN
  - IN (값1, 값2 ... )
  - 값들 중 하나라도 일치
- LIKE
  - 비교 문자열과 형태가 일치
  - 와일드카드 활용
- IS NULL / IS NOT NULL
  - NULL 여부를 확인할 때는 = 대신 IS 사용
- 부정 연산자
  - 같지 않다.
    - !=, ^=, <>
  - ~ 와 같지 않다.
    - NOT 칼럼이름 =
  - ~ 보다 크지 않다.
    - NOT 칼럼이름 >
- 연산자 우선순위
  1. 괄호
  2. NOT
  3. 비교 연산자, SQL
  4. AND
  5. OR

<br>

[목차로 가기](#목차)

<br>

#### 5-2-3. SQLite 집계 함수

<br>

- 각 집합에 대한 계산을 하고 나온 하나의 값을 반환
- 여러 행으로부터 하나의 결괏값을 반환
- SELECT 구문에서만 사용됨
  - COUNT()
  - AVG()
  - MIN(), MAX()
  - SUM()
- INTEGER 일 때만 사용 가능

<br>

[목차로 가기](#목차)

<br>

#### 5-2-4. LIKE

<br>

- 패턴 일치를 기반으로 데이터를 조회
- 두 개의 와일드카드
  - % percent sign
    - 이 자리에 문자열이 있을 수도, 없을 수도 있다.
  - _ underscore
    - 이 자리에 반드시 한 개의 문자가 존재해야 한다.
- 와일드카드 사용례
  - 2%
    - 2 로 시작하는 값
  - %2
    - 2 로 끝나는 값
  - %2%
    - 2 가 들어가는 값
  - _2%
    - 2 앞에 아무 값이 하나가 있고 2로 시작하는 값
  - 1___
    - 1 로 시작하는 네 자리 수
  - 2\_%\_% / 2__%
    - 2 로 시작하고 중간에 두 자리의 값이 있음
    - 2 로 시작하는 적어도 세 자리의 수

<br>

[목차로 가기](#목차)

<br>

#### 5-2-5. ORDER BY

<br>

- 오름차순, 내림차순 정렬

- ASC

- DESC

- ```sql
  SELECT 조회할 대상 FROM 테이블 이름 ORDER BY 대상 필드 ASC;
  SELECT 조회할 대상 FROM 테이블 이름 ORDER BY 대상 필드 DESC;
  ```
  

<br>

[목차로 가기](#목차)

<br>

#### 5-2-6. 기본 함수와 연산

<br>

- 문자열 함수
  - SUBSTR
    - 문자열 자르기
    - SUBSTR(문자열, start, length)
    - 시작 인덱스는 1, 마지막 인덱스는 -1
  - TRIM
    - 문자열 공백 제거
    - TRIM(문자열), LTRIM(문자열), RTRIM(문자열)
  - LENGTH
    - 문자열 길이
    - LENGTH(문자열)
  - REPLACE
    - 패턴에 일치하는 부분을 변경
    - REPLACE(문자열, 패턴, 변경값)
  - UPPER, LOWER
    - 대소문자 변경
    - UPPER(문자열), LOWER(문자열)
  - ||
    - 문자열 합치기
- 숫자 함수
  - ABS(숫자)
  - SIGH(숫자)
    - 부호
  - MOD(숫자1, 숫자2)
    - 숫자1을 숫자2로 나눈 나머지
  - CEIL(숫자), FLOOR(숫자), ROUND(숫자)
  - POWER(숫자1, 숫자2)
    - 숫자1의 숫자2 제곱
  - SQRT(숫자)
- 산술 연산자
  - +, -, *, /

<br>

[목차로 가기](#목차)

<br>

#### 5-2-7. GROUP BY

<br>

- SELECT 문의 optional 절

- GROUP BY 를 통해 지정된 어떤 필드를 기준으로 잡고, 어떤 레코드들이 특정 필드상에서 같은 값을 가지고 있는 경우 그 필드를 기준으로 같은 값을 가지는 레코드 끼리 집단화 시킴

- WHERE 절을 통해 어떤 조건으로 필터링 하고 싶은 경우 반드시 WHERE 뒤에 작성해야 함

  - WHERE 연산이 먼저 이루어짐

- 집계함수와 활용하였을 때 의미가 있다.

- 그룹화된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨진다.

  - ```sql
    SELECT * FROM users GROUP BY last_name;
    ```

  - ```sql
    SELECT last_name "성", COUNT(*) FROM users GROUP BY "성";
    ```

- GROUP BY 절에 명시하지 않은 컬럼은 별도로 지정할 수 없음

  - 그룹마다 하나의 행을 출력하게 되므로 집계함수 등을 활용해야 한다.

- 결과는 정렬되지 않는다.

  - ORDER BY 를 쓰는것이 원칙

- HAVING

  - 집계함수는 연산의 순서상 WHERE 의 조건으로 필터링 할 수 없음

  - HAVING 을 활용하여 조건을 정해준다.

    - ```sql
      SELECT * FROM 테이블 이름 GROUP BY 컬럼1, 컬럼2 HAVING 그룹 조건;
      ```

- SELECT 문장 실행 순서

  1. FROM
  2. WHERE
  3. GROUP BY
  4. HAVING
  5. SELECT
  6. ORDER BY
  7. LIMIT / OFFSET

<br>

[목차로 가기](#목차)

<br>

### 5-3. Update

<br>

- ALTER TABLE

- 테이블 이름 변경

- 새로운 column 추가

  - 이미 필드가 정의된 테이블에 이미 레코드가 추가되어있는 상태라면, 그 이후에 새로운 컬럼을 추가할 경우 NOT NULL 형태의 컬럼은 추가할 수 없다.

  - 레코드 라는 것은 해당 행에 열의 스키마 형식에 맞게 작업을 수행하고 난 결과를 나타내는데, 특정 행이 레코드된 상태에서 세로방향으로 NOT NULL 필드를 만들 때 아무 값이라도 써 넣어 줘야 레코드 된 행, 즉 전체의 행이 온전한 상태를 유지할 수 있기 때문이다.

  - 즉 NOT NULL 은 해당 필드의 스키마일 뿐이고 실제 들어가는 값은 없기 때문에 오류가 난다고 볼 수 있다.

  - 비어있지 말라고 설정을 해주지만 정작 주는 값은 없기때문에 비어버리게 되는 것이다 !!

  - 이 경우 NOT NULL 형식을 피해서 만들거나,

  - 기본 값 DEFAULT 를 설정하면 된다.

    - ```sql
      -- 방법 1
      ALTER TABLE 테이블 이름 ADD COLUMN 컬럼 이름 TEXT;
      -- 방법 2
      ALTER TABLE 테이블 이름 ADD COLUMN 컬럼 이름 TEXT NOT NULL DEFAULT 기본 값;
      ```

- column 이름 수정

- column 삭제

<br>

[목차로 가기](#목차)

<br>

## 6. CASE

<br>

- 특정 상황에서 데이터를 변환하여 활용할 수 있음

- ```sql
  SELECT
  	CASE
  		WHEN 조건식 THEN 식
  		WHEN 조건식 THEN 식
  		ELSE 식
  	END AS ""
  ```

- ELSE 를 생략하는 경우 NULL 이 지정됨

<br>

[목차로 가기](#목차)

<br>

## 7. 서브쿼리

<br>

- 특정 값을 메인 쿼리에 반환하여 활용하는 것

- 실제 테이블에 없는 기준을 이용한 검색이 가능함

- 소괄호로 감싸서 구분해준다

- 서브쿼리는 메인 쿼리의 칼럼을 모두 사용할 수 있지만 그 반대의 경우는 불가능하다.

- ```sql
  SELECT *
  FROM 테이블
  WHERE 컬럼1 =
  (
      SELECT 컬럼1
      FROM 테이블
  );
  ```

- 단일 행 서브쿼리

  - 서브쿼리의 결과가 없거나 한 개인 경우
  - 단일 행 비교 연산자와 함께 사용
    - =
    - <
    - <=
    - \>=
    - <>

- 다중 행 서브쿼리

  - 서브쿼리 결과가 두 개 이상인 경우
  - 다중행 비교 연산자와 함께 사용
    - IN
    - EXISTS
    - 그 외

- 다중 칼럼 서브쿼리

<br>

[목차로 가기](#목차)

<br>

## 8. JOIN

<br>

- 관계형 데이터베이스의 가장 큰 장점이자 핵심 기능
- 테이블을 나눠서 데이터를 저장하고 JOIN 으로 테이블끼리 결합하여 출력하는데 활용
- 기본키 PK 와 외래키 FK 값의 관계에 의해 결합
- 대표적 JOIN
  - INNER JOIN
    - 두 테이블에 조건이 주어졌을 때 모두 일치하는 행만 반환
    - 교집합
  - OUTER JOIN
    - 동일한 값이 없는 행도 반환
    - 두 집합 중 교집합과 나머지 한쪽에 해당하는 부분
    - 기준에 따라 LEFT / RIGHT / FULL 을 지정
  - CROSS JOIN
    - 모든 데이터의 조합
    - JOIN 이 가능한 모든 경우의 수

<br>

[목차로 가기](#목차)

<br>

## 9. 모델링

<br>

- 데이터베이스의 구조나 형식으로 모델 구조만 보고 어떤 데이터를 다루는지 알 수 있음
  - 개념적 데이터 모델링
    - 데이터의 요구사항을 찾고 분석하는 과정
    - 핵심 개체 사이의 관계를 찾아내고 표현
  - 논리적 데이터 모델링
    - 데이터베이스 설계 프로세스의 과정으로 정보의 논리적인 구조와 규칙을 명확하게 표현하는 기법/과정
  - 물리적 데이터 모델링
    - 논리적 데이터 모델이 데이터 저장소로서 어떻게 실제로 저장될 것인가
- ERD - Entity Relation Diagram
  - 개체 관계 모델
  - 주요 용어
    - 엔터티
      - 업무가 관여하는 정보
    - 속성
      - 언터티가 가지는 성격
      - 데이터 타입과 크기 및 제약사항 지정
    - 관계
      - 엔터티 간의 관계, 연관성
- ERD
  - 개체 관계 모델
  - 관계
    - 카디널리티
    - 수적 관계
      - 1:1 관계
        - A는 B를 하나 가진다, B는 A를 하나 가진다
    - 옵셔널리티
    - 1 필수 / 0 선택
- 정규화
  - 데이터베이스 테이블을 설계하는 과정에서 중복성을 제거하여 성능을 향상
  - 조회하는 경우 정규화가 안되어있으면 너무 커다란 데이터를 모두 조회해야 하기 때문에 비 효율적이다.
  - 정규화를 하여 적당한 구분단위로 크기를 조정하여 분류해두면 조회할 때 효율적이다.
  - 정규화의 종류
    - 제 1 정규화
      - 도메인의 원자값
      - 한 속성에 여러 개의 속성이 포함
      - 같은 유형의 속성이 여러 개로 나눠져 있는 경우 제거
    - 제 2 정규화
      - 부분적 함수 종속성 제거
      - PK 가 아닌 모든 칼럼은 PK 에 종속되도록 규정
    - 제 3 정규화
      - 이행적 함수 종속성 제거
      - X >>> Y 그리고 Y >>> Z
      - 일반 속성 간의 함수 종속 관계가 존재하지 않아야 함

<br>

[목차로 가기](#목차)

<br>

## 파이썬-DB 1. ORM

<br>

- Object Relation Mapping

  - 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술
  - 파이썬에서는 SQLAlchemy, peewee 등 라이브러리가 있으며 Django 프레임워크 에서는 내장 Django ORM 을 활용
  - Object 로 DB를 조작한다.

- 모델 설계 및 반영

  1. 클래스를 생성하여 내가 원하는 DB 의 구조를 만든다.
  2. 클래스의 내용으로 DB 에 반영하기 위한 마이그레이션 파일을 생성한다.
     - make migrations
     - `python manage.py makemigrations`
  3. DB 에 migrate 한다.
     - `python manage.py migrate`

- Migration

  - 마이그레이션
  - 모델에 생긴 변화를 DB 에 반영하기 위한 방법
  - 마이그레이션 파일을 만들어 DB 에 스키마를 반영한다.

- DB 조작

  - ClassName.Manager.QuerySet API

    - genre 라는 테이블이 있을 때,
    - `Genre.objects.all()`

  - Create

    1. create 메서드 활용

       - genre 라는 테이블이 있을 때,

       - `Genre.objects.create(name = "발라드")`

    2. 인스턴스로 조작

       ```python
       # genre 라는 테이블이 있을 때
       genre = Genre()
       genre.name = "발라드"
       genre.save()
       ```

  - Read

    1. 전체 데이터 조회
       - `Genre.objects.all()`
    2. 일부 데이터 조회 / get
       - `Genre.objects.get(id = 1)`
       - 단일 객체를 불러올 때 사용
    3. 일부 데이터 조회 / filter
       - `Genre.objects.filter(id = 1)`
       - 여러 객체를 불러올 때 사용

  - Update

    ```python
    # genre 라는 테이블이 있을 때
    genre = Genre.objects.get(id = 1) # genre.name >>> 발라드
    genre.name = "트로트" # genre.name >>> 트로트
    genre.save()
    ```

  - Delete

    ```python
    # genre 라는 테이블이 있을 때
    genre = Genre.objects.get(id = 1)
    genre.delete()
    ```

<br>

[목차로 가기](#목차)

<br>

## 파이썬-DB 2. QuerySet API

<br>

- gt / gte

  - greater then / greater then equal

    ```python
    Entry.objects.filter(id__gt = 4)
    # SELECT ... WHERE id > 4;
    
    Entry.objects.filter(id__gte = 4)
    # SELECT ... WHERE id >= 4;
    ```

- lt / lte

  - less then / less then equal

    ```python
    Entry.objects.filter(id__lt = 4)
    Entry.objects.filter(id__lte = 4)
    
    # SELECT ... WHERE id < 4;
    # SELECT ... WHERE id <= 4;
    ```


- in

  ```python
  Entry.objects.filter(id__in = [1, 3, 4])
  Entry.objects.filter(headline__in = "abc")
  
  # SELECT ... WHERE id IN (1, 3, 4);
  # SELECT ... WHERE headline IN ('a', 'b', 'c');
  ```

- startswith / istartswith

  ```python
  Entry.objects.filter(headline__startswith = "Lennon")
  Entry.objects.filter(headline__istartswith = "Lennon") # 대소문자 구분 X
  
  # SELECT ... WHERE headline LIKE "Lennon%";
  # SELECT ... WHERE headline ILIKE "Lennon%" 대소문자 구분 X
  ```

- endswith

  ```python
  Entry.objects.filter(headline__endswith = "Lennon")
  Entry.objects.filter(headline__iendswith = "Lennon")
  
  # SELECT ... WHERE headline LIKE "%Lennon";
  # SELECT ... WHERE headline ILIKE "%Lennon";
  ```

- contains

  ```python
  Entry.objects.get(headline__contains = "Lennon")
  Entry.objects.get(headline__icontains = "Lennon")
  
  # SELECT ... WHERE headline LIKE "%Lennon%";
  # SELECT ... WHERE headline ILIKE "%Lennon%";
  ```

- range

  ```python
  import datetime
  start_date = datetime.date(2005, 1, 1)
  end_date = datetime.date(2005, 3, 31)
  Entry.objects.filter(pub_date__range = (start_date, end_date))
  
  # SELECT ... WHERE pub_date
  # BETWEEN '2005-01-01' and '2005-03-31';
  ```

- 복합 활용

  ```python
  inner_qs = Blog.objects.filter(name__contains = "Cheddar")
  entries = Entry.objects.filter(blog__in = inner_qs)
  
  # SELECT ... 
  # WHERE blog.id IN
  #	(SELECT id FROM ... WHERE NAME LIKE "%Cheddar%")
  ```

- 활용

  ```python
  Entry.objects.all()[0]
  
  # SELECT ... 
  # LIMIT 1;
  ```

  ```python
  Entry.objects.order_by("id")
  
  # SELECT ... 
  # ORDER BY id;
  ```

  ```python
  Entry.objects.order_by("-id")
  
  # SELECT ... 
  # ORDER BY id DESC;
  ```

<br>

[목차로 가기](#목차)

<br>

## 파이썬-DB 3. ORM 확장

<br>

- 어떤 테이블이 다른 테이블로부터 FK키를 받아오면서 구성될 때 종속관계가 있다고 할 수 있다.

  ```python
  class Genre(models.Model):
  	name = models.CharField(max_length = 30)
  
  class Artist(models.Model):
  	name = models.CharField(max_length = 30)
  	debut = models.DateField()
  
  class Album(models.Model):
  	name = models.CharField(max_length =30)
  	genre = models.ForeignKey('Genre', on_delete = models.CASCADE) # 종속
  	artist = models.ForeignKey('Artist', on_delete = models.CASCADE) # 종속
  ```

  - 이와 같이 테이블을 구성하면 Album 테이블에는
    - name 필드와,
    - genre 대신 genre_id,
    - artist 대신 artist_id,

  - 라는 필드가 생긴다.

- Foreign Key
  - 외래키
  - 키를 이용하여 부모 테이블의 유일한 값을 참조
    - 참조 무결성
      - 데이터베이스 관계 모델에서 관련된 두 개의 테이블 간의 일관성
  - 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 한다.
- models.ForeignKey 필드
  - 두 개의 필수 위치 인자
    - Model class
      - 참조하는 모델
    - on_delete
      - 외래 키가 참조하는 객체가 삭제되었을 때 처리하는 방식
      - CASCADE
        - 부모 객체(참조된 객체) 가 삭제 되었을 때 이를 참조하는 객체도 삭제
      - PROTECT
        - 삭제되지 않음
      - SET_NULL
        - NULL 설정
      - SET_DEFAULT
        - 기본 값 설정

- 참조와 역참조

  ```python
  # 참조
  album = Album.objects.get(id = 1)
  album.artist
  # <Artist: Artist object (1)>
  album.genre
  # <Genre: Genre object (1)>
  
  # 역참조
  genre = Genre.objects.get(id = 1)
  genre.album_set.all()
  # <QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]
  ```

  - 첫 번째 글자는 소문자로 쓰고 언더바 셋을 하면 일반적으로 역참조를 하겠다는 약속이다.
  - Album 테이블에 genre 객체가 있고 genre 는 테이블 즉,
  - genre 테이블이 Album 테이블에 속해있는 상태에서,
  - genre 테이블에서 Album 테이블로 역참조를 하려고 할 때,
    - Album_set >>> X
    - album_set >>> O
  - 이와 같이 하위 테이블에서 상위 테이블로 역참조를 할 수 있다.

<br>

[목차로 가기](#목차)

<br>