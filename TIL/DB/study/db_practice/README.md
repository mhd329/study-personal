# 사전 설정

## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
id PRIMARY KEY,        
sido INTEGER NOT NULL, 
gender INTEGER NOT NULL,
age INTEGER NOT NULL,  
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,   
va_left REAL NOT NULL, 
va_right REAL NOT NULL,

blood_pressure INTEGER 
NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);
```

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
select count(*) from healthcare where age < 10;
```

```
count(*)
--------
156277
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
select count(*) from healthcare where gender=1;
```

```
count(*)
--------
510689
```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
select count(*) from healthcare where smoking=3 and is_drinking=1;
```

```
count(*)
--------
150361
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
select count(*) from healthcare where va_left=2.0 and va_right=2.0;
```

```
count(*)
--------
1692
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
select DISTINCT sido from healthcare;
```

```
sido
----
36
27
11
31
41
44
48
30
42
43
46
28
26
47
45
29
49
```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

> 예) 허리 둘레가 x이상이면서 몸무게가 y이하인 사람
>
> ```sql
> -- 허리둘레와 혈압을 중복없이 출력
> select DISTINCT waist, blood_pressure from healthcare;
> 
> -- 허리둘레가 77 이하인 사람의 수
> select count(*) from healthcare where waist <= 77;
> 
> -- 혈압이 100 이하인 사람의 수
> select count(*) from healthcare where blood_pressure <= 100;
> 
> -- 허리둘레 77 이하이면서 혈압이 100 이하인 사람의 수
> select count(*) from healthcare where waist <= 77 and blood_pressure <= 100;
> 
> -- 나이가 18세 이상인 사람의 수
> select count(*) from healthcare where age >= 18;
> 
> -- 조건 여러개 연습
> select count(*) from healthcare where age = 18 and weight >= 70 and height >= 165 and waist < 70;
> 
> select id from healthcare where age = 18 and weight >= 70 and height >= 165 and waist < 70;
> 
> select waist from healthcare where age = 18 and weight >= 70 and height >= 165;
> 
> select id from healthcare where age = 18 and weight >= 70 and height >= 165 limit 10;
> 
> select id from healthcare where age = 18 and weight >= 70 and height >= 165 limit 10 offset 5;
> ```