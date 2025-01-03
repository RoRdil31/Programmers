SELECT COUNT(*) AS FISH_COUNT,
       MAX(LENGTH) AS MAX_LENGTH,
       FISH_TYPE
    FROM FISH_INFO
    GROUP BY 3
      HAVING (AVG(CASE
                    WHEN LENGTH > 10 THEN LENGTH
                    ELSE 10
                  END) >= 33)
    ORDER BY 3














# SELECT COUNT(*)    AS FISH_COUNT, 
#        MAX(LENGTH) AS MAX_LENGTH, 
#        FISH_TYPE
#     FROM FISH_INFO
#     GROUP BY FISH_TYPE
#       HAVING AVG(CASE
#                     WHEN LENGTH > 10 THEN LENGTH
#                     ELSE 10
#                  END) >= 33
#     ORDER BY FISH_TYPE