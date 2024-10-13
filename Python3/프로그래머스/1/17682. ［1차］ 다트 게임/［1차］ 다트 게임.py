# import re

# def SDT(num, c):
#     if c == 'S' : return num
#     elif c == 'D' : return num ** 2
#     else : return num ** 3
    
# def solution(dartResult):
#     answer = []
#     dart = re.findall(r'\d+|[a-zA-Z][^\d\s]*',dartResult) # 숫자 또는 문자+특수문자 조합 찾음
    
#     for idx, chars in zip(range(1,len(dart)+1,2),dart[1::2]):
#         answer.append(SDT(int(dart[idx-1]),chars[0])) # 숫자,(Single/Double/Triple 연산)
#         if len(chars) == 2 : 
#             if chars[1] == '*':
#                 answer[len(answer)-1] *= 2
#                 if len(answer) != 1 : answer[len(answer)-2] *= 2
#             elif chars[1] == '#':
#                 answer[len(answer)-1] *= (-1)
    
#     return sum(answer)

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    # print(dart) 
    
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    # print(dart)
    answer = sum(dart)
    return answer