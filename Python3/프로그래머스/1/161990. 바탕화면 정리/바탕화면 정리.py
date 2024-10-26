def solution(wallpaper):
    lux,luy, rdx,rdy = -1,-1,-1,-1
        
    for idx,i in enumerate(wallpaper): # 시작 지점 찾기.
        if lux == -1 and '#' in i : 
            lux = idx
            luy = i.index('#')
        elif '#' in i :
            if i.index('#') < luy : luy = i.index('#')
        
        if '#' in i and i.rindex('#') > rdy : rdy = i.rindex('#')
        
    for idx,i in enumerate(wallpaper[::-1]):
        if '#' in i :
            rdx = len(wallpaper)-idx
            break
    
    return [lux, luy, rdx, rdy+1]