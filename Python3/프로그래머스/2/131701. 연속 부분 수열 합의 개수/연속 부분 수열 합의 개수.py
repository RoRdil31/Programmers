def solution(elements):
    answer = []
    circle = elements*2
    for i,num in enumerate(elements):
        answer.append(num)
        for num2 in circle[i+1:i+len(elements)]:
            num += num2
            answer.append(num)
            
    return len(set(answer))
    
    
    
    
    
    
    
    
    
    
#     answer = 0
    
#     sums, n = [], len(elements)
#     elements += elements[:-1]
#     for i,a in enumerate(elements):
#         sums.append(a)
#         for b in elements[i+1:i+n]:
#             a += b
#             sums.append(a)
#     # print(len(list(set(sums))))
        
#     return len(list(set(sums)))