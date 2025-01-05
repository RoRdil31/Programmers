from collections import Counter
def solution(topping):
    cnt = 0
    p2 = Counter(topping)
    p1 = set()
    for i in topping:
        p2[i] -= 1
        if p2[i] == 0 : del p2[i]
        p1.add(i)
        if len(p1) == len(p2): cnt += 1
        
    return cnt














# from collections import Counter
# def solution(topping):
#     answer = 0
#     p1 = Counter(topping)
#     p2 = set()
#     for i in topping:
#         p1[i] -= 1
#         if p1[i] == 0 : del p1[i]
#         p2.add(i)
#         if len(p1) == len(p2) : answer += 1
    
#     return answer