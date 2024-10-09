def solution(food):
    answer = ''
    for idx,n in enumerate(food):
        answer += str(idx)*(n//2)
    
    # return answer+'0'+''.join(sorted(answer,reverse=True))
    return answer+'0'+answer[::-1]
