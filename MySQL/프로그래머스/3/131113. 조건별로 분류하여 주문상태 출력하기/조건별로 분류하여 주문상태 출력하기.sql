SELECT order_id
        , product_id
        , DATE_FORMAT(out_date, '%Y-%m-%d') AS 'out_date'
        , CASE
            WHEN out_date <= '2022-05-02' THEN '출고완료'
            WHEN out_date IS NULL THEN '출고미정'
            ELSE '출고대기'
        END AS '출고여부'
    FROM food_order
    order by 1
    












# SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE,'%Y-%m-%d'), CASE
#     WHEN DATEDIFF('2022-05-01', OUT_DATE) >= 0 THEN '출고완료'
#     WHEN DATEDIFF('2022-05-01', OUT_DATE) < 0 THEN '출고대기'
#     ELSE '출고미정' END AS 출고여부
#     FROM FOOD_ORDER
#     ORDER BY ORDER_ID