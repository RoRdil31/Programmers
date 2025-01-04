def solution(clothes):
    answer = 1
    d = {i[1]:[None] for i in clothes}
    for c, i in clothes: d[i].append(c)
    for k, v in d.items():
        answer *= len(v)
    
    return answer - 1
















# def solution(clothes):
#     result = 1
#     c = {i[1]:1 for i in clothes}
#     for name, s in clothes:
#         c[s] += 1
    
#     for i in c.values():
#         result = result * i
#     return result - 1