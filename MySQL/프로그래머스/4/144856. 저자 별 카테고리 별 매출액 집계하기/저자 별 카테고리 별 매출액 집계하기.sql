SELECT 
        A.AUTHOR_ID
        , AUTHOR_NAME
        , CATEGORY
        , SUM(PRICE * SALES) AS TOTAL_SALES
FROM BOOK_SALES S
JOIN BOOK B ON S.BOOK_ID = B.BOOK_ID
JOIN AUTHOR A ON B.AUTHOR_ID = A.AUTHOR_ID
WHERE SALES_DATE LIKE '2022-01%'
GROUP BY 1, 2, 3
ORDER BY 1, 3 DESC


















# SELECT A.AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(PRICE*SALES) AS TOTAL_SALES
#     FROM BOOK B
#     JOIN AUTHOR A
#       ON B.AUTHOR_ID = A.AUTHOR_ID
#     JOIN BOOK_SALES S
#       ON B.BOOK_ID = S.BOOK_ID
#     WHERE SALES_DATE LIKE '2022-01%'
#     GROUP BY A.AUTHOR_ID, CATEGORY
#     ORDER BY A.AUTHOR_ID, CATEGORY DESC