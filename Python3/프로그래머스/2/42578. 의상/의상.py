def solution(clothes):
    c = {i[1]:0 for i in clothes}
    for name, s in clothes:
        # if not c[s]: c[s] = [name]
        # else : c[s].append(name)
        c[s] += 1
    
    answer = 1
    for i in c.values():
        answer = answer * (i + 1)
    return answer - 1