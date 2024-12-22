from collections import deque
import copy
def solution(maps):
    height, weight = len(maps), len(maps[0])
    maps.insert(0, 'X'*weight)
    maps.append('X'*weight)
    maps = ['X'+m+'X' for m in maps]
    queue = deque()
    for idx, m in enumerate(maps):
        if 'S' in m: queue.append((idx, m.index('S'), 0)); break
    maps = [[i for i in m] for m in maps]
    
    dx = [0,1,0,-1] # 아래, 오, 위, 왼
    dy = [1,0,-1,0]
    def found_LorE(tg):
        visited = copy.deepcopy(maps) # 깊은 복사 (원본에 영향 X)
        while queue:
            h, w, v = queue.popleft()
    
            for xx, yy in zip(dx, dy):
                nx, ny = w+xx, h+yy
                if visited[ny][nx] == tg: return (ny, nx, v+1)
                
                if visited[ny][nx] != 'X' : 
                    visited[ny][nx] = 'X'
                    queue.append((ny, nx, v+1))
        
        return -1
    
    start = found_LorE('L')
    if start == -1 : return -1
    queue = deque()
    queue.append(start)
    end = found_LorE('E')
    if end == -1 : return -1

    return end[2]