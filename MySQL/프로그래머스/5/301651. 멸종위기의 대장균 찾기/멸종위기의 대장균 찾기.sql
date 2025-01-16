WITH RECURSIVE GENERATION AS(
    SELECT ID, PARENT_ID, 1 AS LV
        FROM ECOLI_DATA
        WHERE PARENT_ID IS NULL
    UNION ALL
    SELECT E.ID, E.PARENT_ID, LV + 1
        FROM ECOLI_DATA E JOIN GENERATION G
          ON E.PARENT_ID = G.ID
)
SELECT COUNT(A.ID) AS COUNT, A.LV AS GENERATION
    FROM GENERATION A LEFT JOIN GENERATION B
      ON A.ID = B.PARENT_ID
    WHERE B.ID IS NULL
    GROUP BY 2
    ORDER BY 2