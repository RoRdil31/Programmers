SELECT FLOOR(PRICE/10000)*10000 AS PRICE_GROUP, COUNT(*) AS PRODUCTS
    FROM PRODUCT
    GROUP BY 1
    ORDER BY 1
    




















# # SELECT PRICE_GROUP, COUNT(*) AS PRODUCTS
# #     FROM (SELECT *,CASE 
# #         WHEN PRICE < 10000 THEN 0
# #         WHEN PRICE < 20000 THEN 10000
# #         WHEN PRICE < 30000 THEN 20000
# #         WHEN PRICE < 40000 THEN 30000
# #         WHEN PRICE < 50000 THEN 40000
# #         WHEN PRICE < 60000 THEN 50000
# #         WHEN PRICE < 70000 THEN 60000
# #         WHEN PRICE < 80000 THEN 70000
# #         WHEN PRICE < 90000 THEN 80000
# #         WHEN PRICE < 100000 THEN 90000
# #         ELSE 100000 END AS PRICE_GROUP FROM PRODUCT) AS SUB
# #     GROUP
# #        BY PRICE_GROUP
# #     ORDER
# #        BY PRICE_GROUP

# SELECT FLOOR(PRICE / 10000)*10000 AS PRICE_GROUP, COUNT(*) AS PRODUCTS
#     FROM PRODUCT
#     GROUP BY 1
#     ORDER BY 1