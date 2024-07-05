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
SELECT count(*) FROM healthcare;
-- 02
SELECT MAX(age), MIN(age) FROM healthcare;
-- 03
SELECT MAX(height), MIN(weight) FROM healthcare;
-- 04
SELECT count(*) FROM healthcare WHERE height BETWEEN 160 and 170;
-- 05
SELECT waist FROM healthcare WHERE is_drinking = 1 and waist not LIKE '' ORDER BY waist DESC LIMIT 5;
-- 06
SELECT count(*) FROM healthcare WHERE va_left >= 1.5 and va_right >= 1.5 and is_drinking = 1;
-- 07
SELECT count(*) FROM healthcare WHERE blood_pressure < 120;
-- 08
SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;
-- 09
SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender = 1;
-- 10
SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1;
-- 아래는 안됨
-- SELECT id, height, weight FROM healthcare WHERE height = MAX(height) ORDER BY weight DESC LIMIT 10;
-- 11
SELECT count(*) FROM healthcare WHERE weight * 10000 / (height * height) >= 30;
-- 12
SELECT id, weight * 10000 / (height * height) AS BMI FROM healthcare WHERE smoking = 3 ORDER BY weight * 10000 / (height * height) DESC LIMIT 5;
-- 13
SELECT id AS "ID" FROM healthcare LIMIT 5;
-- 14
SELECT * FROM healthcare WHERE (va_left >= 2.0 AND va_right >= 2.0) AND va_left + va_right >= 4.0 LIMIT 10;
-- 15
SELECT id, ((va_left + va_right) / 2) AS "TOP 10 AVG va" FROM healthcare WHERE (va_left >= 1.0 AND va_right >= 1.0) AND va_left + va_right >= 4.0 LIMIT 10;