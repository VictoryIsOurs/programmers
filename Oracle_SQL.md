## SELECT
- 출제 빈도 낮음
- 평균 점수 높음
- 조건에 맞는 레코드를, 원하는 순서대로. 기본기를 처음부터 탄탄히 다져보세요.<br/><br/>


#### 모든 레코드 조회하기 : 동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요
~~~sql
select * from ANUMAL_INS
order by ANIMAL_ID;
~~~

#### 역순 정렬하기 : 동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 ANIMAL_ID 역순으로 보여주세요.
~~~sql
select NAME, DATETIME 
from ANUMAL_INS
order by ANIMAL_ID desc;
~~~

#### 아픈 동물 찾기 : 동물 보호소에 들어온 동물 중 아픈 동물1의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.
~~~sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
order by ANIMAL_ID;
~~~

#### 어린 동물 찾기 : 동물 보호소에 들어온 동물 중 젊은 동물1의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.
~~~sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
order by ANIMAL_ID;
~~~

### 여러 기준으로 정렬하기 (****) : 동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.
~~~sql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
order by NAME, DATETIME desc;
~~~

### (******) : 상위 n개 레코드 :  동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.
~~~sql
SELECT NAME
FROM (SELECT * FROM ANIMAL_INS order by DATETIME)
WHERE rownum = 1;
~~~

### 최댓값 구하기 : 가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
--- 오라클의 경우, FROM에 따로 만들어줘야 하는 듯
~~~sql
SELECT DATETIME
FROM (SELECT * FROM ANIMAL_INS ORDER BY DATETIME DESC)
WHERE rownum = 1; 
~~~

~~~sql
SELECT AGE, NAME
FROM AGETABLE
WHERE AGE = (SELECT MAX(AGE) FROM AGETABLE);
~~~

### 최솟값 구하기 : 동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
~~~sql
SELECT DATETIME
FROM (SELECT * FROM ANIMAL_INS ORDER BY DATETIME)
where rownum = 1; 

SELECT MIN(DATETIME) as "시간"
FROM ANIMAL_INS
ORDER BY DATETIME;
~~~

~~~sql
SELECT count(ANIMAL_ID) as "count"
FROM ANIMAL_INS;
~~~

### 중복 제거하기 : 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.
~~~sql
SELECT count(distinct(NAME))
FROM ANIMAL_INS
WHERE NAME is not NULL;   -- != 쓰지 않기, "NULL" 쓰지 않기!
~~~

### 고양이와 개는 몇 마리 있을까 : 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.
~~~sql
SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) as "count"
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
order by ANIMAL_TYPE asc; //or asc는 빼도 됨.
~~~


### 동명 동물 수 찾기 : 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.
~~~sql
SELECT NAME, COUNT(NAME) as COUNT
FROM ANIMAL_INS
WHERE NAME is not NULL
GROUP BY NAME
having count(NAME) >= 2
ORDER BY NAME;
~~~

### 입양 시각 구하기(1) oracle
~~~
DATE 자료형 컬럼을 시간별로 추출하고 GROUP BY절을 활용하여 해결할 수 있습니다.

먼저, 자료형이 DATE인 DATETIME컬럼의 시간을 추출하기 위해 to_char를 이용합니다.

09:00부터 19:59까지의 데이터만 조회할 것이므로 where 조건에 Between 09 and 19를 추가합니다.

그리고 해당 시간을 기준으로 GROUP BY, ORDER BY를 사용하여 그룹화/정렬화 합니다.

참고 : GROUP BY절을 사용할 경우 해당 컬럼과 그룹함수만 사용할 수 있습니다.
~~~
~~~sql
SELECT TO_CHAR(DATETIME, 'HH24')as HOUR, COUNT(ANIMAL_ID) as COUNT
FROM ANIMAL_OUTS
WHERE TO_CHAR(DATETIME, 'HH24') between 09 and 19
GROUP BY TO_CHAR(DATETIME, 'HH24')
ORDER BY TO_CHAR(DATETIME, 'HH24')
~~~

### ★★★★★★★입양 시각 구하기(2) : 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
~~~sql
SELECT HOUR, COUNT(B.DATETIME) AS COUNT
FROM
(
    SELECT LEVEL-1 AS HOUR
    FROM DUAL
    CONNECT BY LEVEL <= 24
)A LEFT JOIN ANIMAL_OUTS B
ON A.HOUR = TO_CHAR(B.DATETIME, 'HH24')
GROUP BY HOUR
ORDER BY HOUR;
~~~

![image](https://user-images.githubusercontent.com/48751536/142750617-c32e7cc3-d5b6-4c32-8c15-85eb3a638956.png)

### 없어진 기록 찾기 : 천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
~~~sql
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS A, ANIMAL_OUTS B
WHERE A.ANIMAL_ID(+) = B.ANIMAL_ID and A.ANIMAL_ID is null
ORDER BY B.ANIMAL_ID
~~~

### 있었는데요 없었습니다 : 관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다. 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.
~~~sql
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A, ANIMAL_OUTS B
WHERE A.ANIMAL_ID = B.ANIMAL_ID and A.DATETIME > B.DATETIME
ORDER BY A.DATETIME
~~~


### 
~~~sql
SELECT * FROM ( SELECT ANIMAL_INS.NAME, ANIMAL_INS.DATETIME FROM ANIMAL_INS LEFT OUTER JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID WHERE ANIMAL_OUTS.ANIMAL_ID IS NULL ORDER BY ANIMAL_INS.DATETIME ) WHERE ROWNUM <= 3;

출처: https://youngsubee.tistory.com/entry/SQL-오랜-기간-보호한-동물1-풀것 [기록]
~~~

-----------------------------------------------------------------------
----------------------------------------------------------------------
-----------------------------------------------------------------------
-----------------------------------------------------------------------
-----------------------------------------------------------------------
-----------------------------------------------------------------------
-----------------------------------------------------------------------
-----------------------------------------------------------------------
