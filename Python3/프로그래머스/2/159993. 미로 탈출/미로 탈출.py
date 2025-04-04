from collections import deque
def solution(maps):
    rows, cols = len(maps), len(maps[0])
    ways = [(1,0),(0,1),(0,-1),(-1,0)]
    now = [(row, m.index('S')) for row,m in enumerate(maps) if 'S' in m][0]
    now = (now[0],now[1],0)
    
    def find_LE(tg):
        visited = [[i for i in m] for m in maps]
        visited[now[0]][now[1]] = 'X'
        queue = deque([now])
        
        while queue:
            x,y,v = queue.popleft()
        
            for dx, dy in ways:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and visited[nx][ny] != 'X':
                    if visited[nx][ny] == tg: return (nx,ny,v+1)
                    queue.append((nx,ny,v+1))
                    visited[nx][ny] = 'X'
                    
        return -1
    
    now = find_LE('L')
    if now == -1 : return -1
    now = find_LE('E')
    if now == -1 : return -1
    
    return now[2]






















# from collections import deque
# import copy
# def solution(maps):
#     height, weight = len(maps), len(maps[0])
#     maps.insert(0, 'X'*weight)
#     maps.append('X'*weight)
#     maps = ['X'+m+'X' for m in maps]
#     queue = deque()
#     for idx, m in enumerate(maps):
#         if 'S' in m: queue.append((idx, m.index('S'), 0)); break
#     maps = [[i for i in m] for m in maps]
    
#     dx = [0,1,0,-1] # 아래, 오, 위, 왼
#     dy = [1,0,-1,0]
#     def found_LorE(tg): # BFS.
#         visited = copy.deepcopy(maps) # 깊은 복사 (원본에 영향 X)
#         while queue:
#             h, w, v = queue.popleft()
    
#             for xx, yy in zip(dx, dy):
#                 nx, ny = w+xx, h+yy
#                 if visited[ny][nx] == tg: return (ny, nx, v+1)
                
#                 if visited[ny][nx] != 'X' : 
#                     visited[ny][nx] = 'X'
#                     queue.append((ny, nx, v+1))
        
#         return -1
    
#     start = found_LorE('L')
#     if start == -1 : return -1
#     queue = deque()
#     queue.append(start)
#     end = found_LorE('E')
#     if end == -1 : return -1

#     return end[2]