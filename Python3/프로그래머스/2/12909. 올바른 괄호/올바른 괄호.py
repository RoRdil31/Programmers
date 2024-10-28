
def solution(s):
    stack = []
    for i in s:
        if not stack : stack.append(i); continue
        if stack[-1] =='(' and i==')' : stack.pop()
        else : stack.append(i)
    
    return False if stack else True
    
    
    
    
    
    
    
    
    
    
    
    
    
#     HavetoBreak = False
#     ex = [i for i in ex]
#     # ex.append('.')
    
#     limit = 0
#     # i = 0
#     if ex[-1] == '(' or ex[0] == ')': return False

#     cnt1 = 0
    
#     for p in ex:
#         if p == '(': cnt1 += 1
#         else : cnt1 -= 1
        
#         if cnt1 < 0 :
#             HavetoBreak = True
#             break
            
#     if HavetoBreak == True or cnt1!=0: return False
#     else : return True
