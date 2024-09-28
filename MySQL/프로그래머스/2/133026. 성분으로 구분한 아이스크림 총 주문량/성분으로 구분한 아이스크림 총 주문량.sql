
SELECT INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
    FROM FIRST_HALF A
    JOIN ICECREAM_INFO B
      ON A.FLAVOR = B.FLAVOR
    GROUP
       BY INGREDIENT_TYPE
       