## Select

#### 모든 레코드 조회하기
~~~sql
SELECT * from ANIMAL_INS
order by ANIMAL_ID;
~~~
--------------------------------------------
#### 역순 배열 - desc 사용
~~~sql
SELECT NAME, DATETIME
from ANIMAL_INS   --- select 어떤걸 해줘야 하는지 잘 보기
order by ANIMAL_ID desc;
~~~
---------------------------

### 제약 조건 넣기
동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.
~~~sql
SELECT NAME, DATETIME from ANIMAL_INS
order by ANIMAL_ID desc;
~~~
-------------------------


## 상위 n개의 레코드 (limit !!!) 
~~~MySQL
MySQL의 경우 : NAME 값을 조회하는데 가장 맨 위 행 1개만을 조회하기 위해 LIMIT 구문을 사용해야 합니다.
LIMIT 1 : 맨 위에서부터 1개까지의 정보 조회
LIMIT 3 : 맨 위에서부터 3개까지의 정보 조회
LIMIT 2, 6 : 위에서 2번째부터 6번째까지의 정보 조회
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1
~~~

~~~sql
SELECT NAME
from ANIMAL_INS
order by DATETIME
limit 1;
~~~
--------------------------

## 가장 최근에 들어온 동물 확인
~~~sql
SELECT DATETIME
from ANIMAL_INS
order by DATETIME desc   --가장 최근의 들어온 경우는 역순정렬이므로 desc를 해줘야 가장 최신이 위에 나옴.
limit 1;    --레코드 하나만 추출
~~~
-----------------------------

## 중복 제거하기 (☆☆☆☆☆☆) ☆☆☆☆☆ distinct
~~~sql
select count(distinct(NAME))   --☆☆☆☆☆ distinct가 들어가는 부분 잘 보기
from ANIMAL_INS
where NAME is not null    -- null이 아니라는 제약조건 꼭 보기
~~~
--------------------------------

## 개와 고양이 구분해주기
~~~sql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) 
FROM ANIMAL_INS 
GROUP BY ANIMAL_TYPE 
ORDER BY ANIMAL_TYPE  ---개와 고양이를 구분해주라고 했으니,, 이게 들어가야 함!
~~~

-----------------------------

## 동명 동물 수 찾기
~~~sql
SELECT NAME, count(NAME)
FROM ANIMAL_INS
WHERE NAME is NOT NULL
GROUP BY NAME
HAVING COUNT(NAME) >= 2  -- 그룹바이 안에서의 조건 명시 
order by NAME asc
~~~
---------------------------

## 입양시각 구하기(1)
~~~sql
SELECT HOUR(DATETIME) as HOUR , count(ANIMAL_ID) as COUNT  ---시간 구할 떄는 HOUR(  ) 함수 쓰기!!!
from ANIMAL_OUTS
where HOUR(DATETIME) BETWEEN 9 and 19 
group by HOUR(DATETIME)
order by HOUR(DATETIME) asc;
~~~
-----------------------

## NULL처리하기 
IFNULL(컬럼명, NULL 시 값);

~~~sql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') , SEX_UPON_INTAKE
from ANIMAL_INS
order by ANIMAL_ID
~~~

-----------------------

## 없어진 기록 찾기 (left outer join ~~ on ~~ where ~)
~~~sql
--왼쪽 테이블을 기준으로 비교한다.
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
from ANIMAL_OUTS
left outer join ANIMAL_INS 
on ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
where ANIMAL_INS.ANIMAL_ID is null
order by ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
~~~


----------------------
## 오랜기간 보호한 동물(1)
~~~sql
SELECT ANIMAL_INS.NAME, ANIMAL_INS.DATETIME
from ANIMAL_INS
left join ANIMAL_OUTS
on ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
where ANIMAL_OUTS.ANIMAL_ID is null
order by ANIMAL_INS.DATETIME asc
limit 3;
~~~

---------------------

## 보호소에서 중성화한 동물
~~~sql
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.ANIMAL_TYPE, ANIMAL_INS.NAME
from ANIMAL_INS
left join ANIMAL_OUTS
on ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
where ANIMAL_INS.SEX_UPON_INTAKE like '%Intact%' and (ANIMAL_OUTS.SEX_UPON_OUTCOME like '%Spayed%' or ANIMAL_OUTS.SEX_UPON_OUTCOME like '%Neutered%')
order by ANIMAL_INS.ANIMAL_ID
~~~

-------------------------

## DATE형 변환
~~~sql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') as '날짜'
from ANIMAL_INS
order by ANIMAL_ID;
~~~
-----------------------------


##인터넷 예제 : 환승역 출력
~~~sql
select COLOR, count(COLOR)
from line as A
left join line as B
on A.id = B.id
order by 제약조건;
