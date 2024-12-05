from collections import Counter
def solution(topping):
    answer = 0
    p1 = Counter(topping)
    p2 = set()
    for i in topping:
        p1[i] -= 1
        if p1[i] == 0 : del p1[i]
        p2.add(i)
        if len(p1) == len(p2) : answer += 1
    
    return answer