SELECT 
        MEMBER_NAME
        , REVIEW_TEXT
        , DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d')AS REVIEW_DATE
FROM MEMBER_PROFILE M
JOIN REST_REVIEW R ON M.MEMBER_ID = R.MEMBER_ID
  
WHERE M.MEMBER_ID = (SELECT MEMBER_ID
                    FROM REST_REVIEW
                    GROUP BY 1
                    ORDER BY COUNT(REVIEW_ID) DESC
                    LIMIT 1)


ORDER BY 3, 2














# WITH MOST_MEMBER AS(
#     SELECT MEMBER_ID, COUNT(*)
#         FROM REST_REVIEW
#         GROUP BY MEMBER_ID
#         ORDER BY 2 DESC
#         LIMIT 1
# )
# SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
#     FROM REST_REVIEW R
#     JOIN MOST_MEMBER M
#       ON R.MEMBER_ID = M.MEMBER_ID
#     JOIN MEMBER_PROFILE P
#       ON P.MEMBER_ID = M.MEMBER_ID
#     ORDER BY 3, 2
    

# # M : 회원 ID, 회원 이름, 회원 연락처, 성별, 생년월일

# # R : 리뷰 ID, 식당 ID, 회원 ID, 점수, 리뷰 텍스트, 리뷰 작성일














# # SELECT M.MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE,'%Y-%m-%d')
# #     FROM REST_REVIEW A
# #     JOIN (SELECT MEMBER_ID 
# #                 FROM REST_REVIEW
# #                 GROUP BY MEMBER_ID
# #                 ORDER BY COUNT(*) DESC
# #                 LIMIT 1) B
# #       ON A.MEMBER_ID = B.MEMBER_ID
# #     JOIN MEMBER_PROFILE M
# #       ON M.MEMBER_ID = A.MEMBER_ID
# #     ORDER BY REVIEW_DATE, REVIEW_TEXT