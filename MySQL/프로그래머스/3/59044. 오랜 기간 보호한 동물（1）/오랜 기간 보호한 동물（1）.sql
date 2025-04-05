select 
    i.name
    , i.datetime
    from animal_ins i left join animal_outs o on i.animal_id = o.animal_id
    where o.animal_id IS NULL
    order by 2
    limit 3
    














# SELECT NAME, DATETIME
#     FROM ANIMAL_INS
#     WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS)
#     ORDER BY DATETIME
#     LIMIT 3