def solution(food):
    ans = ''
    for idx, i in enumerate(food[1:], start=1):
        cnt = i//2
        ans += str(idx)*cnt
    
    return ans + '0' + ans[::-1]















# def solution(food):
#     answer = ''
#     for idx,n in enumerate(food):
#         answer += str(idx)*(n//2)
    
#     # return answer+'0'+''.join(sorted(answer,reverse=True))
#     return answer+'0'+answer[::-1]