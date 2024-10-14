SELECT CART_ID
    FROM (SELECT CART_ID
            FROM CART_PRODUCTS
            GROUP BY CART_ID, NAME
            HAVING NAME REGEXP 'Milk|Yogurt') AS S
    GROUP BY CART_ID
      HAVING COUNT(CART_ID) = 2
# SELECT CART_ID, NAME
#                 FROM CART_PRODUCTS
#                 GROUP BY CART_ID, NAME
#                   HAVING NAME REGEXP 'Milk|Yogurt' 