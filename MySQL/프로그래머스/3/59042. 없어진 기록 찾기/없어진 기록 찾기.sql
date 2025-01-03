SELECT ANIMAL_ID, NAME
    FROM ANIMAL_OUTS
    WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID
                                FROM ANIMAL_INS)
    ORDER BY 1


# I : 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부

# O : 이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부












# SELECT ANIMAL_ID, NAME
#     FROM ANIMAL_OUTS 
#     WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID
#                               FROM ANIMAL_INS)
#     ORDER BY ANIMAL_ID
    
# SELECT ANIMAL_ID, NAME FROM ANIMAL_OUTS
# EXCEPT
# SELECT ANIMAL_ID, NAME FROM ANIMAL_INS