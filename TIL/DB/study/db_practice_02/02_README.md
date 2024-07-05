# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

### table 및 스키마 조회

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

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT count(*) FROM healthcare;
```

```
count(*)
--------
1000000
```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 

```sql
SELECT MAX(age), MIN(age) FROM healthcare;
```

```
MAX(age)  MIN(age)
--------  --------
18        9
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT MAX(height), MIN(weight) FROM healthcare;
```

```
MAX(height)  MIN(weight)
-----------  -----------
195          30
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
SELECT count(*) FROM healthcare WHERE height BETWEEN 160 and 170;
```

```
count(*)
--------
516930
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. 

```sql
SELECT waist FROM healthcare WHERE is_drinking = 1 and waist not LIKE '' ORDER BY waist DESC LIMIT 5;
```

```
waist
-----
146.0
142.0
141.4
140.0
140.0
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT count(*) FROM healthcare WHERE va_left >= 1.5 and va_right >= 1.5 and is_drinking = 1;
```

```
count(*)
--------
36697
```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
SELECT count(*) FROM healthcare WHERE blood_pressure < 120;
```

```
count(*)
--------
360808
```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;
```

```
AVG(waist)      
----------------
85.8665098512525
```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender = 1;
```

```
AVG(height)       AVG(weight)     
----------------  ----------------
167.452735422145  69.7131620222875
```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1;
```

```
id      height  weight
------  ------  ------
836005  195     110
```

### 11. BMI가 30이상인 사람의 수를 출력하시오. 

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT count(*) FROM healthcare WHERE weight * 10000 / (height * height) >= 30;
```

```
count(*)
--------
53121
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT id, weight * 10000 / (height * height) AS BMI FROM healthcare WHERE smoking = 3 ORDER BY weight * 10000 / (height * height) DESC LIMIT 5;
```

```
id      BMI
------  ---
231431  50
934714  49
722707  48
947281  47
948801  47
```

### 13. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
SELECT id AS "ID" FROM healthcare LIMIT 5;
```

```
ID   
-----
1
10
100
1000
10000
```

### 14. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
SELECT * FROM healthcare WHERE (va_left >= 2.0 AND va_right >= 2.0) AND va_left + va_right >= 4.0 LIMIT 10;
```

```
id    sido  gender  age  height  weight  waist  va_left  va_right  blood_pressure  smoking  is_drinking
----  ----  ------  ---  ------  ------  -----  -------  --------  --------------  -------  -----------
2032  11    2       10   160     60      74.0   2.0      2.0       110             1        1
2130  41    1       12   165     65      78.0   2.0      2.0       140             2        1
2902  41    1       12   170     90      103.5  2.0      2.0       116             2        1
2991  41    2       9    165     55      66.0   2.0      2.0       100             1        0
3864  44    1       9    170     70      87.0   2.0      2.0       107             1        1
4144  28    1       11   165     60      77.0   2.0      2.0       133             1        1
5003  28    1       9    165     75      83.0   2.0      2.0       118             1        0
5249  26    1       16   170     70      84.0   9.9      9.9                       1        0
5729  46    1       10   175     95      93.0   2.0      2.0       115             1        0
5820  41    1       9    165     65      81.0   2.0      2.0       136             1        1
```

### 15. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
SELECT id, ((va_left + va_right) / 2) AS "TOP 10 AVG va" FROM healthcare WHERE (va_left >= 1.0 AND va_right >= 1.0) AND va_left + va_right >= 4.0 LIMIT 10;
```

```
id    TOP 10 AVG va
----  -------------
201   5.55
1369  5.45
2032  2.0
2130  2.0
2402  5.45
2892  5.7
2902  2.0
2991  2.0
3864  2.0
4034  5.45
```