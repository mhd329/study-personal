-- 허리둘레와 혈압을 중복없이 출력
select DISTINCT waist, blood_pressure from healthcare;

-- 허리둘레가 77 이하인 사람의 수
select count(*) from healthcare where waist <= 77;

-- 혈압이 100 이하인 사람의 수
select count(*) from healthcare where blood_pressure <= 100;

-- 허리둘레 77 이하이면서 혈압이 100 이하인 사람의 수
select count(*) from healthcare where waist <= 77 and blood_pressure <= 100;

-- 나이가 18세 이상인 사람의 수
select count(*) from healthcare where age >= 18;

-- 조건 여러개 연습
select count(*) from healthcare where age = 18 and weight >= 70 and height >= 165 and waist < 70;

select id from healthcare where age = 18 and weight >= 70 and height >= 165 and waist < 70;

select waist from healthcare where age = 18 and weight >= 70 and height >= 165;

select id from healthcare where age = 18 and weight >= 70 and height >= 165 limit 10;

select id from healthcare where age = 18 and weight >= 70 and height >= 165 limit 10 offset 5;