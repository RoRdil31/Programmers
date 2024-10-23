def solution(park, routes): # W E
    loc = [-1,-1]
    lh, lw = len(park), len(park[0])
    way = {'E':(0,1), 'N':(-1,0), 'W':(0,-1), 'S':(1,0)}
    
    for idx,p in enumerate(park): # 시작 지점 찾음.
        if p.find('S') != -1 : loc = [idx, p.find('S')]
        
    pre_loc = loc.copy()
    for route in routes:
        op, n = route.split(' ')
        n = int(n)
        
        loc[0] += way[op][0]*n
        loc[1] += way[op][1]*n
        
        if not(0<=loc[0]<lh and 0<=loc[1]<lw) : loc = pre_loc.copy(); continue # 공원 벗어나면 이전 loc.
        
        if (op=='W' or op=='E'):
            min_loc,max_loc = min(pre_loc[1],loc[1]), max(pre_loc[1],loc[1])
            if 'X' in park[loc[0]][min_loc:max_loc+1]: # 좌우 가는 길 'X' 여부 확인.
                loc = pre_loc.copy()
    
        else : 
            is_X = False
            min_loc,max_loc = min(pre_loc[0],loc[0]), max(pre_loc[0],loc[0])
            for p in park[min_loc:max_loc+1]: # 상하 가는 길 'X' 여부 확인.
                if p[loc[1]] == 'X': is_X = True; break
            
            if is_X : loc = pre_loc.copy(); continue # 가는 길 'X'가 없는 경우에만 이동.
        
        pre_loc = loc.copy()
        
    return loc
    
#     # now2 = now.copy()
#     prev_now = now.copy()

#     # 공원 벗어나면 False.
#     # if not(0<=now[0]<len(park) or 0<=now[1]<len(park[0])): return prev_now
    
#     if op=='E': 
#         if not(0<=now[1]+n<len(park[0])): return prev_now
#         for i in range(now[1]+1,now[1]+n+1):
#             if 'X' == park[now[0]][i] : return prev_now
#         now[1] += n
#     elif op=='W': 
#         if not(0<=now[1]-n<len(park[0])): return prev_now
#         for i in range(now[1]-n,now[1]):
#             if 'X' == park[now[0]][i] : return prev_now
#         now[1] -= n
#     elif op=='N': 
#         if not(0<=now[0]-n<len(park)): return prev_now
#         for i in range(now[0]-n,now[0]):
#             if 'X' == park[i][now[1]] : return prev_now
#         now[0] -= n
#     else : 
#         if not(0<=now[0]+n<len(park)): return prev_now
#         for i in range(now[0]+1,now[0]+n+1):
#             if 'X' == park[i][now[1]] : return prev_now
#         now[0] += n
    
    

    
#     return now


# def solution(park, routes):
    
#     # row_len = len(park)
#     # col_len = len(park[0])
#     # set start point
#     now = [i for i,str1 in enumerate(park) if 'S' in str1]
#     now.append(park[now[0]].index('S'))
    
    
    
#     for r in routes :
#         op, n = r.split(' ')
#         n = int(n)
        
#         now = possible(op,n,now,park)

        
#     #     print(now)
        
    
#     # print()
#     return now