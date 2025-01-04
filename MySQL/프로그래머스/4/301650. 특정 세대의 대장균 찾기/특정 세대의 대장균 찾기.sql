# WITH RECURSIVE GENERATION AS(
#     SELECT ID, PARENT_ID, 1 AS LV
#         FROM ECOLI_DATA
#         WHERE PARENT_ID IS NULL
#     UNION ALL
#     SELECT E.ID, E.PARENT_ID, G.LV + 1
#         FROM ECOLI_DATA E
#         INNER JOIN GENERATION G
#         ON E.PARENT_ID = G.ID
# )
# SELECT ID
#     FROM GENERATION
#     WHERE LV = 3
#     ORDER BY ID
SELECT A.ID
FROM ECOLI_DATA AS A
JOIN ECOLI_DATA AS B ON A.PARENT_ID = B.ID
JOIN ECOLI_DATA AS C ON B.PARENT_ID = C.ID
WHERE C.PARENT_ID IS NULL
ORDER BY A.ID ASC;