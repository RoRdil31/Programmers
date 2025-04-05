SELECT ID, FISH_NAME, LENGTH
FROM (SELECT ID, FISH_TYPE, LENGTH, MAX(LENGTH) OVER(PARTITION BY FISH_TYPE) AS MAX_LENGTH
        FROM FISH_INFO
     ) I
JOIN FISH_NAME_INFO N
  ON I.FISH_TYPE = N.FISH_TYPE
WHERE LENGTH = MAX_LENGTH 
ORDER BY 1











# SELECT id
#         , fish_name
#         , length
#     FROM (select *, 
#             max(length) over(partition by fish_type) as max_length
#             from fish_info) i
#     join fish_name_info n on i.fish_type = n.fish_type
#     where length = max_length
#     order by 1














# # select 
# #         id
# #         , fish_name
# #         , length
# #     from (select *, max(length) over(partition by fish_type) as max_len
# #             from fish_info) s
# #     join fish_name_info n
# #       on s.fish_type = n.fish_type
# #     where length = max_len
    
# #     order by 1
















# # # # SELECT ID, FISH_NAME, LENGTH
# # # #     FROM (SELECT *, MAX(LENGTH) OVER(PARTITION BY FISH_TYPE) AS MAX_LEN
# # # #             FROM FISH_INFO) I
# # # #     JOIN FISH_NAME_INFO N ON I.FISH_TYPE = N.FISH_TYPE
# # # #     WHERE LENGTH = MAX_LEN
# # # #     ORDER BY 1




















# # # # SELECT ID, FISH_NAME, LENGTH
# # # #     FROM FISH_INFO I
# # # #     JOIN FISH_NAME_INFO N
# # # #       ON I.FISH_TYPE = N.FISH_TYPE
# # # #     WHERE I.LENGTH = (
# # # #         SELECT MAX(I2.LENGTH)
# # # #         FROM FISH_INFO I2
# # # #         WHERE I.FISH_TYPE = I2.FISH_TYPE)
# # # #     ORDER BY 1