SELECT ID, LENGTH
    FROM (SELECT *, ROW_NUMBER() OVER (ORDER BY LENGTH DESC, ID) AS 순위
          FROM FISH_INFO 
    
    ) FISH_INFO
    WHERE 순위 <= 10;

