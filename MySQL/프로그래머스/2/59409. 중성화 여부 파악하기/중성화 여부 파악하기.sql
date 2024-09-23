-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, 중성화
    FROM (SELECT *,
                CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%' 
                        OR SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
                     ELSE 'X' END AS 중성화
          FROM ANIMAL_INS
          )AS A
    ORDER
       BY ANIMAL_ID