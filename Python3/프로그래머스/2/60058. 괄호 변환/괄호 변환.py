from collections import deque
def is_correct(u):
    queue = deque(u)
    stack = []
    while queue:
        v = queue.popleft()
        if not stack : stack.append(v)
        elif stack[-1]=='(' and v==')': stack.pop()
        else : stack.append(v)
    return not stack

def solution(p):
    if not p : return '' # 1번
    answer = ''
    u, v = 0, 0
    
    for i in range(2,len(p)+1,2): # 2번
        u = p[:i]
        if u.count('(') == u.count(')'):
            v = p[i:]
            break
            
    if is_correct(u): return u + solution(v) # 3번
    else: answer = '('+ solution(v) + ')' + ''.join(['(' if i==')' else ')' for i in u[1:-1]]) # 4번
        
    return answer


# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
#   4-3. ')'를 다시 붙입니다. 
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
#   4-5. 생성된 문자열을 반환합니다.