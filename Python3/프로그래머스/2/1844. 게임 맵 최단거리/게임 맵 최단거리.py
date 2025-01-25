import copy
from collections import deque
def solution(maps):
    ways = [(0,1), (1,0), (-1,0), (0,-1)]
    rows, cols = len(maps), len(maps[0])
    goal = [rows-1, cols-1]
    
    def bfs(start):
        visited = copy.deepcopy(maps)
        queue = deque([start])
        
        while queue:
            x, y, v = queue.popleft()
            for dx, dy in ways:
                nx, ny = x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and visited[nx][ny]!=0:
                    if goal == [nx,ny]: return v+1
                    queue.append((nx,ny,v+1))
                    visited[nx][ny] = 0
        
        return -1
    
    answer = bfs([0,0,1])
    
    return answer




















# from collections import deque
# def solution(maps):
#     rows, cols = len(maps), len(maps[0])
#     goal = [rows-1, cols-1]
#     ways = [(1,0),(0,1),(-1,0),(0,-1)]
#     queue = deque()
    
#     def bfs(queue):
        
#         while queue:
#             x, y, cnt = queue.popleft()
        
#             if [x,y] == goal: return cnt

#             for dx, dy in ways:
#                 nx, ny = x+dx, y+dy
#                 if (0<=nx<rows) and (0<=ny<cols) and maps[nx][ny]==1 :
#                     maps[nx][ny] = 0
#                     queue.append( (nx, ny, cnt+1) )
        
#         return -1
    
#     queue.append((0,0,1))
#     result = bfs(queue)
    
#     return result



# from collections import deque
# def solution(maps):
#     answer, x, y = 0, 1, 1
#     add = [0]*(len(maps[0]))
#     goal = [len(maps), len(maps[0])]
#     maps.insert(0,add)
#     for m in maps:
#         m.insert(0,0)
#         m.append(0)
#     maps.append(add)
#     maps[1][1] = 0
    
#     queue = deque()
#     dx = [0,1,0,-1] # 아래, 오, 위, 왼
#     dy = [1,0,-1,0]
#     queue.append((x,y,1))
    
#     while(queue):
#         x,y,cnt = queue.popleft()
#         if (x==goal[0] and y==goal[1]) : 
#             return cnt
#         for xx, yy in zip(dx, dy):
#             nx = x+xx
#             ny = y+yy
#             if (maps[nx][ny] == 1):
#                 maps[nx][ny] = 0
#                 queue.append((nx,ny,cnt+1))
#     return -1
