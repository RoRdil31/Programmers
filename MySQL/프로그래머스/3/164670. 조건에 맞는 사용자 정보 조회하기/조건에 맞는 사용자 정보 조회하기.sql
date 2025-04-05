SELECT USER_ID
        , NICKNAME
        , CONCAT(CITY,' ', STREET_ADDRESS1,' ', STREET_ADDRESS2) AS '전체주소'
        , CONCAT(SUBSTR(TLNO,1,3),'-',SUBSTR(TLNO,4,4),'-',SUBSTR(TLNO,8,4) ) AS '전화번호'
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_USER U
  ON B.WRITER_ID = U.USER_ID
GROUP BY WRITER_ID
  HAVING COUNT(BOARD_ID) >= 3



ORDER BY 1 DESC














# SELECT USER_ID, NICKNAME,
#        CONCAT(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) AS '전체주소',
#        CONCAT(SUBSTR(TLNO,1,3),'-',SUBSTR(TLNO,4,4),'-',SUBSTR(TLNO,8)) AS '전화번호'
#     FROM USED_GOODS_BOARD AS B
#     JOIN USED_GOODS_USER AS U
#       ON B.WRITER_ID = U.USER_ID
#     GROUP BY WRITER_ID HAVING COUNT(BOARD_ID) >= 3
#     ORDER BY 1 DESC



# # B : 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수

# # U : 회원 ID, 닉네임, 시, 도로명 주소, 상세 주소, 전화번호












# # SELECT USER_ID, NICKNAME, 
# #         CONCAT(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) AS 전체주소,
# #         CONCAT(SUBSTR(TLNO,1,3),'-',SUBSTR(TLNO,4,4),'-',SUBSTR(TLNO,8,4)) AS 전화번호
# #     FROM USED_GOODS_USER
# #     WHERE USER_ID IN (SELECT WRITER_ID
# #                         FROM USED_GOODS_BOARD
# #                         GROUP BY WRITER_ID
# #                         HAVING COUNT(BOARD_ID) >= 3)
# #     ORDER BY USER_ID DESC