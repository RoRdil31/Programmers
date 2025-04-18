SELECT YEAR(SALES_DATE) YEAR
        , MONTH(SALES_DATE) MONTH
        , GENDER
        , COUNT(DISTINCT S.USER_ID) USERS

FROM USER_INFO U
JOIN ONLINE_SALE S ON U.USER_ID = S.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY 1,2,3
ORDER BY 1,2,3















# SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, GENDER, COUNT(DISTINCT(U.USER_ID)) AS USERS
#     FROM USER_INFO U
#     JOIN ONLINE_SALE S
#       ON U.USER_ID = S.USER_ID
#     WHERE GENDER IS NOT NULL
#     GROUP BY YEAR, MONTH, GENDER
#     ORDER BY YEAR, MONTH, GENDER