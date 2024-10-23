def solution(ingredient):
    answer = 0
    stack = []
    
    for i in ingredient:
        stack.append(i) 
        if stack[-4:] == [1,2,3,1] : answer += 1; del stack[-4:]
    
    return answer


# Time Complexity : O(n^2)

# hamberger = "1231"
# str_ing = ''.join(map(str,ingredient))
# while hamberger in str_ing :
#         answer += 1
#         str_ing = str_ing.replace(hamberger,'',1)