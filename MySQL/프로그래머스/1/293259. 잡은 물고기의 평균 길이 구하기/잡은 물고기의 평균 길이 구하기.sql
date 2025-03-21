select round(avg(if(length is null, 10, length)), 2) as average_length
    from fish_info
    













# SELECT ROUND(AVG(
#     CASE WHEN LENGTH < 10 THEN 10
#          WHEN LENGTH IS NULL THEN 10
#          ELSE LENGTH
#     END
#     ),2) AS AVERAGE_LENGTH
#     FROM FISH_INFO


# # SELECT (30+50+40+20+10+10)/6 => 26.6667