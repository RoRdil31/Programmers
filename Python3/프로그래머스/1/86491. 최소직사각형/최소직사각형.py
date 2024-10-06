def solution(sizes):
    row_max, col_max = 0,0
    for s in sizes:
        row_max = max(max(s[0],s[1]),row_max)# if max(s[0],s[1]) > row_max else row_max
        col_max = max(min(s[0],s[1]),col_max)# if min(s[0],s[1]) > col_max else col_max
        
    return row_max * col_max