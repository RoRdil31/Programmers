def solution(lottos, win_nums):
    score = 0
    hidden_score = 0
    
    for l in lottos:
        if l==0 : hidden_score += 1
        elif l in win_nums : 
            score += 1
            win_nums.remove(l)
    if score+hidden_score == 0 : hidden_score = 1
    return [7-score-hidden_score, (7-score) if score!=0 else 6]