SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY
FROM ITEM_INFO I
LEFT JOIN ITEM_TREE T
  ON I.ITEM_ID = T.PARENT_ITEM_ID
WHERE T.ITEM_ID IS NULL

ORDER BY 1 DESC
















# select 
#         i.item_id
#         , item_name
#         , rarity
#     from item_info i
#     left join item_tree t
#            on i.item_id = t.parent_item_id
#     where t.parent_item_id is null
#     order by 1 desc














# # SELECT P.ITEM_ID, ITEM_NAME, RARITY
# #     FROM ITEM_INFO P
# #     LEFT
# #     JOIN ITEM_TREE C
# #       ON P.ITEM_ID = C.PARENT_ITEM_ID
# #     WHERE PARENT_ITEM_ID IS NULL
# #     ORDER BY 1 DESC