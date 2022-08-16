# Database

<br>

### 1. 관계형 데이터베이스

<br>

- RDB
  - 관계형 데이터베이스
  - keys, values 간의 관계를 table 로 정리한 것
- schema
  - 자료의 구조, 표현 방법, 관계등의 표현 방식에 대한 약속의 집합
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

### 2. SQLite

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

### 3. SQL

<br>

- Keywords
  - INSERT
  - SELECT
  - UPDATE
  - DELETE

<br>

### 4. Hello World !

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
    SECECT * FROM examples;
    ```

  - 특정 테이블의 레코드 정보를 반환

-  terminal view switching

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

### 5. CRUD

<br>

###### 1. Create

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

###### 2. Read

- SELECT
- 테이블에서 데이터 조회
- 다양한 절(clause) 과 함께 사용
- SELECT +
  - ORDER BY
  - DISTINCT
  - WHERE
  - LIMIT +
    - OFFSET
  - GROUP BY