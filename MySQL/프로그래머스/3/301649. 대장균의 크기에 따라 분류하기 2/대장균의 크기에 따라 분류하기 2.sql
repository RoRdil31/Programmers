SELECT ID, 
        CASE
            WHEN RANKS <= 0.25 THEN 'CRITICAL'
            WHEN RANKS <= 0.5 THEN 'HIGH'
            WHEN RANKS <= 0.75 THEN 'MEDIUM'
            ELSE 'LOW'
        END AS COLONY_NAME
    FROM (SELECT ID, 1-PERCENT_RANK() OVER(ORDER BY SIZE_OF_COLONY) AS RANKS
            FROM ECOLI_DATA) AS SUB 
    ORDER BY 1

# SELECT ID,SIZE_OF_COLONY, 1-PERCENT_RANK() OVER(ORDER BY SIZE_OF_COLONY)
#             FROM ECOLI_DATA

















# # SELECT ID, 
# #         CASE 
# #             WHEN S.RANKS/CNTS <= 0.25 THEN 'CRITICAL'
# #             WHEN S.RANKS/CNTS <= 0.5 THEN 'HIGH'
# #             WHEN S.RANKS/CNTS <= 0.75 THEN 'MEDIUM'
# #             ELSE 'LOW'
# #         END AS COLONY_NAME
# #     FROM (SELECT *, 
# #             RANK() OVER(ORDER BY SIZE_OF_COLONY DESC) AS RANKS, 
# #             COUNT(*) OVER() AS CNTS
# #           FROM ECOLI_DATA) AS S
# #     ORDER BY 1