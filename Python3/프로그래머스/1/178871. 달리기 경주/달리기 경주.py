def solution(players, callings):
    
    ranking = {players[i]:i for i in range(len(players))}
    
    for c in callings:
        now = ranking[c]
        players[now-1], players[now] = players[now], players[now-1]
        
        ranking[c] -= 1
        ranking[players[now]] += 1
    
    return players
    
    
    
#     answer = []
    
#     ranking={player:int(idx) for idx,player in enumerate(players)}

#     for call in callings:
#         current_rank=ranking[call]

#         ranking[call]-=1
#         ranking[players[current_rank-1]]+=1

#         players[current_rank],players[current_rank-1] = players[current_rank-1],call
           
    
#     return players