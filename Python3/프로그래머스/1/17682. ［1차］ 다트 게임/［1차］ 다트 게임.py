import re

def SDT(num, c):
    if c == 'S' : return num
    elif c == 'D' : return num ** 2
    else : return num ** 3
    
def solution(dartResult):
    answer = []
    dart = re.findall(r'\d+|[a-zA-Z][^\d\s]*',dartResult) # 숫자 또는 문자+특수문자 조합 찾음
    for idx, chars in zip(range(1,len(dart)+1,2),dart[1::2]):
        answer.append(SDT(int(dart[idx-1]),chars[0])) # 숫자,(Single/Double/Triple 연산)
        if len(chars) == 2 : 
            if chars[1] == '*':
                answer[len(answer)-1] *= 2
                if len(answer) != 1 : answer[len(answer)-2] *= 2
            elif chars[1] == '#':
                answer[len(answer)-1] *= (-1)
    
    return sum(answer)

# 스타상 (*) => 해당 점수, 직전 점수 2배로 만듦. 
    #           (첫번째로 나오면 그 것만 2배) (스타/아차 중첩가능)
# 아차상 (#) => 해당 점수 감점.