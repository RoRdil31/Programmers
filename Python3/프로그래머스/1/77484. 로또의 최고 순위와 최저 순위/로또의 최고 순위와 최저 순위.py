def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    cnt = 0
    hidden_cnt = lottos.count(0)
    
    for i in lottos:
        if i in win_nums: cnt += 1
    
    return [rank[cnt + hidden_cnt],rank[cnt]]
#     score = 0
#     hidden_score = 0
    
#     for l in lottos:
#         if l==0 : hidden_score += 1
#         elif l in win_nums : 
#             score += 1
#             win_nums.remove(l)
            
#     if score+hidden_score == 0 : hidden_score = 1
    
#     return [7-score-hidden_score, (7-score) if score!=0 else 6]