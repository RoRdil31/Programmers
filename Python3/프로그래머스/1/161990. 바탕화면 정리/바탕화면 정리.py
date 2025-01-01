def solution(wallpaper):
    lux, luy, rdx, rdy = -1, 50, -1, -1
    for idx, row in enumerate(wallpaper): # lux
        if '#' in row : lux = idx; break
    for idx, row in enumerate(wallpaper[::-1]): # rdx
        if '#' in row : rdx = len(wallpaper) - idx; break
    for row in wallpaper: # luy
        if '#' in row and row.index('#') < luy: luy = row.index('#')
    for row in wallpaper: # rdy
        if '#' in row and len(row) - (row[::-1].index('#')) > rdy: rdy = len(row) - (row[::-1].index('#'))
    
    return [lux, luy, rdx, rdy]


















# def solution(wallpaper):
#     x = []
#     y = []
    
#     for idxY,i in enumerate(wallpaper):
#         for idxX,j in enumerate(i):
#             if j=='#':
#                 x.append(idxX)
#                 y.append(idxY)
    
#     return [min(y), min(x), max(y)+1, max(x)+1]

# #     lux,luy, rdx,rdy = -1,-1,-1,-1
        
# #     for idx,i in enumerate(wallpaper): # 시작 지점 찾기.
# #         if lux == -1 and '#' in i : 
# #             lux = idx
# #             luy = i.index('#')
# #         elif '#' in i :
# #             if i.index('#') < luy : luy = i.index('#')
        
# #         if '#' in i and i.rindex('#') > rdy : rdy = i.rindex('#')
        
# #     for idx,i in enumerate(wallpaper[::-1]):
# #         if '#' in i :
# #             rdx = len(wallpaper)-idx
# #             break
    
# #     return [lux, luy, rdx, rdy+1]