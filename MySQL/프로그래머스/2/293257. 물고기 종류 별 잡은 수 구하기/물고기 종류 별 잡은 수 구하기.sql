SELECT COUNT(*) AS FISH_COUNT, FISH_NAME
    FROM FISH_INFO AS F, FISH_NAME_INFO AS N
    WHERE F.FISH_TYPE = N.FISH_TYPE
    GROUP BY 2
    ORDER BY 1 DESC



# F :  ID, 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 물고기를 잡은 날짜

# N : 물고기의 종류(숫자), 물고기의 이름(문자)








# SELECT COUNT(*) AS FISH_COUNT, FISH_NAME
#     FROM FISH_INFO A
#     JOIN FISH_NAME_INFO B
#       ON A.FISH_TYPE = B.FISH_TYPE
#     GROUP BY FISH_NAME
#     ORDER BY 1 DESC