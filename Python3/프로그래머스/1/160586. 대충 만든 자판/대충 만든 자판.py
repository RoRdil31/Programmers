def solution(keymap, targets):
    answer = []
    
    for target in targets:
        sum_, fail = 0, False
        for t in target:
            min_index = 999
            for key in keymap:
                min_index = key.find(t) if key.find(t) != -1 and key.find(t) <= min_index else min_index
            
            if min_index == 999 : fail = True ; break
            sum_ += min_index+1
        
        if fail : answer.append(-1)
        else : answer.append(sum_)
    
    return answer