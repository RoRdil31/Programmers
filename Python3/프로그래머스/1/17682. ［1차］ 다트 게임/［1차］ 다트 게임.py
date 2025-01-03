import re
def solution(dartResult):
    answer = []
    scores = re.findall(r'\d+|[SDT*#]+', dartResult)
    
    for i in range(0,len(scores),2):
        if scores[i+1][0]=='D': answer.append(int(scores[i])**2)
        elif scores[i+1][0]=='T': answer.append(int(scores[i])**3)
        else : answer.append(int(scores[i]))
        
        if len(scores[i+1])==2:
            if scores[i+1][1]=='#': answer.append(answer.pop()*(-1))
            else : 
                answer[-1] *= 2
                if len(answer) > 1 : answer[-2] *= 2
    
    return sum(answer)





















# import re
# def solution(dartResult):
#     scores = [0]
#     d = re.findall(r'\d+|[^\d]*', dartResult)
    
#     for i in range(0,len(d)-1,2):
#         score = int(d[i])
#         if d[i+1][0] == 'D': score **= 2
#         elif d[i+1][0] == 'T': score **= 3
        
#         if len(d[i+1]) == 2:
#             if d[i+1][1] == '*': scores[-1] = scores[-1]*2; score *= 2
#             elif d[i+1][1] == '#': score = -score
        
#         scores.append(score)
        
#     return sum(scores)

# # * 이전,현재 2배
# # # 현재 마이너스
















# # # import re

# # # def SDT(num, c):
# # #     if c == 'S' : return num
# # #     elif c == 'D' : return num ** 2
# # #     else : return num ** 3
    
# # # def solution(dartResult):
# # #     answer = []
# # #     dart = re.findall(r'\d+|[a-zA-Z][^\d\s]*',dartResult) # 숫자 또는 문자+특수문자 조합 찾음
    
# # #     for idx, chars in zip(range(1,len(dart)+1,2),dart[1::2]):
# # #         answer.append(SDT(int(dart[idx-1]),chars[0])) # 숫자,(Single/Double/Triple 연산)
# # #         if len(chars) == 2 : 
# # #             if chars[1] == '*':
# # #                 answer[len(answer)-1] *= 2
# # #                 if len(answer) != 1 : answer[len(answer)-2] *= 2
# # #             elif chars[1] == '#':
# # #                 answer[len(answer)-1] *= (-1)
    
# # #     return sum(answer)

# # import re

# # def solution(dartResult):
# #     bonus = {'S' : 1, 'D' : 2, 'T' : 3}
# #     option = {'' : 1, '*' : 2, '#' : -1}
# #     p = re.compile('(\d+)([SDT])([*#]?)')
# #     dart = p.findall(dartResult)
# #     # print(dart) 
    
# #     for i in range(len(dart)):
# #         if dart[i][2] == '*' and i > 0:
# #             dart[i-1] *= 2
# #         dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
# #     # print(dart)
# #     answer = sum(dart)
# #     return answer