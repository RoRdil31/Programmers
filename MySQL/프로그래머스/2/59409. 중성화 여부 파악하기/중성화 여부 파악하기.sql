# SELECT ANIMAL_ID, NAME, 중성화
#     FROM (SELECT *,
#                 CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%' 
#                         OR SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
#                      ELSE 'X' END AS 중성화
#           FROM ANIMAL_INS
#           )AS A
#     ORDER
#        BY ANIMAL_ID



-- LIKE 사용. 더 간단화
# SELECT ANIMAL_ID, NAME,
#         CASE
#             WHEN SEX_UPON_INTAKE LIKE '%Neutered%'
#                 OR SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
#             ELSE 'X'
#         END 중성화
#     FROM ANIMAL_INS
#     ORDER BY ANIMAL_ID
    
    
    
-- REGEXP 정규식 사용

SELECT ANIMAL_ID, NAME,
        CASE
            WHEN SEX_UPON_INTAKE REGEXP 'Neutered|Spayed' THEN 'O'
            ELSE 'X'
        END 중성화
    FROM ANIMAL_INS
    ORDER BY ANIMAL_ID
