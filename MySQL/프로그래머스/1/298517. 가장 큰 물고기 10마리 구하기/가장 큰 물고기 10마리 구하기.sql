SELECT ID, LENGTH
    FROM FISH_INFO 
    ORDER BY LENGTH DESC, ID
    LIMIT 10














# SELECT ID, LENGTH
#     FROM (SELECT *, ROW_NUMBER() OVER (ORDER BY LENGTH DESC, ID) AS 순위
#           FROM FISH_INFO 
    
#     ) FISH_INFO
#     WHERE 순위 <= 10;

# # SELECT *, ROW_NUMBER() OVER (ORDER BY LENGTH DESC, ID) AS 순위
# #           FROM FISH_INFO