-- 테이블 만들기
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
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare

-- 보기좋게 출력
.headers on
.mode column

-- 01
SELECT smoking AS "흡연 여부", COUNT(*) FROM healthcare WHERE "흡연 여부" <> '' GROUP BY "흡연 여부";
-- 02
SELECT is_drinking "음주 여부", COUNT(*) FROM healthcare WHERE "음주 여부" <> '' GROUP BY "음주 여부";
-- 03
SELECT is_drinking "음주 여부", COUNT(*) "혈압 200 이상" FROM healthcare WHERE blood_pressure <> '' AND blood_pressure >= 200 GROUP BY "음주 여부";
-- 04
SELECT sido "시/도", COUNT(*) "명" FROM healthcare WHERE sido <> '' GROUP BY sido HAVING COUNT(*) >= 50000;
-- 05
SELECT height "cm", COUNT(*) "명" FROM healthcare GROUP BY height ORDER BY height DESC LIMIT 5;
-- 06
-- COUNT(*) 된 값을 다룰 때 연산의 순서 상, ORDER BY 는 SELECT 이후에 이루어지므로 HAVING 을 안해주어도 되는 것 같다.
SELECT height "cm", weight "kg", COUNT(*) FROM healthcare GROUP BY cm, kg ORDER BY COUNT(*) DESC LIMIT 5;
-- 07
SELECT is_drinking "음주 여부", AVG(waist) "cm", COUNT(*) "명" FROM healthcare WHERE is_drinking != '' GROUP BY is_drinking;
-- 08
SELECT gender "성별", AVG(va_left) "좌", AVG(va_right) "우" FROM healthcare GROUP BY gender;
-- 09
SELECT age "나이", AVG(height) "평균 키", AVG(weight) "평균 몸무게" FROM healthcare GROUP BY age HAVING "평균 키" >= 160 and "평균 몸무게" >= 60;
-- 10
SELECT
    is_drinking "음주 여부",
    smoking "흡연 여부",
    AVG(weight*10000/(height*height)) "평균 BMI"
FROM
    healthcare
WHERE
    is_drinking <> '' AND
    smoking <> ''
GROUP BY
    is_drinking, smoking;