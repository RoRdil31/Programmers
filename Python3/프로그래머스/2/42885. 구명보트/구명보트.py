def solution(people, limit):
    cnt = 0
    people = sorted(people,reverse=True)
    
    for i in people:
        total = i
        if total + people[-1] <= limit : people.pop()
        cnt += 1
            
    return cnt
    
    
    
#     cnt = 0
#     people.sort(reverse=True)
#     first, last = 0, len(people)-1
    
#     while first <= last:
#         if people[first] + people[last] > limit: first += 1
#         else : first +=1; last -=1
        
#         cnt += 1
        
#     return cnt
