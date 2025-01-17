def solution(participant, completion):
    
    part = {}
    
    for p in participant:
        if p in part : part[p] += 1
        else : part[p] = 1
    
    for c in completion:
        part[c] -= 1
    
    return ''.join([name for name in part if part[name] == 1])
    
    
#     left = ''.join([i for i in participant if i not in completion])
    
#     if not left :
#         for i in participant:
#             if participant.count(i) > 1 : return i
    
#     return left