# def solution(sizes):
#     row_max, col_max = 0,0
#     for s in sizes:
#         row_max = max(max(s[0],s[1]),row_max)
#         col_max = max(min(s[0],s[1]),col_max)
        
#     return row_max * col_max

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)