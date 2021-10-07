## Select

#### 모든 레코드 조회하기
~~~sql
SELECT * from ANIMAL_INS
order by ANIMAL_ID;
~~~
--------------------------------------------
#### 역순 배열 - desc 사용
~~~sql
SELECT NAME, DATETIME from ANIMAL_INS   --- select 어떤걸 해줘야 하는지 잘 보기
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


## 상위 n개의 레코드 
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



