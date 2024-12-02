def solution(clothes):
    result = 1
    c = {i[1]:1 for i in clothes}
    for name, s in clothes:
        c[s] += 1
    
    for i in c.values():
        result = result * i
    return result - 1