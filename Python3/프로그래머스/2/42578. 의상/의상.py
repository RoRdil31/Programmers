def solution(clothes):
    result = 1
    c = {i[1]:0 for i in clothes}
    for name, s in clothes:
        c[s] += 1
    
    for i in c.values():
        result = result * (i + 1)
    return result - 1