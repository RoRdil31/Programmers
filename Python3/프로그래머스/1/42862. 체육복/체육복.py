def solution(n, lost, reserve):
    # students = [1 if i not in lost else 0 for i in range(n+2)]
    students = [1]*(n+2)
    for i in lost:
        if i in reserve: reserve.remove(i); continue
        students[i] = 0
        
    for i in sorted(reserve):
        if students[i-1] == 0 : students[i-1] = 1
        elif students[i+1] == 0 : students[i+1] = 1
        
    return sum(students)-2















# def solution(n, lost, reserve):
    
#     students = [1]*(n+2)
#     for i in lost : 
#         if i in reserve : reserve.remove(i);continue
#         students[i] = 0
        
#     # for i in reserve : 
#     #     if students[i] == 0 : students[i] = 1 ;reserve.remove(i)
#     for i in sorted(reserve) :
#         if  students[i-1] == 0 : students[i-1] = 1
#         elif students[i+1] == 0 : students[i+1] = 1

#     return sum(students)-2