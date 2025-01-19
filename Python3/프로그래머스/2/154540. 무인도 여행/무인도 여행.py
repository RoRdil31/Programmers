from collections import deque
def solution(maps):
    answer = []
    rows, cols = len(maps), len(maps[0])
    ways = [(1,0), (0,1), (0,-1), (-1,0)]
    maps = [[i for i in m] for m in maps]
    
    def bfs(start):
        s = 0
        x,y = start
        first = int(maps[i][j])
        maps[x][y] = 'X'
        queue = deque([start])
        
        while queue:
            x,y = queue.popleft()
            for dx, dy in ways:
                nx, ny = x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and maps[nx][ny]!='X':
                    s += int(maps[nx][ny])
                    queue.append((nx,ny))
                    maps[nx][ny] = 'X'
        answer.append(s+first)
    
    
    while (rows*cols) != sum(m.count('X') for m in maps):
        b = False
        for i in range(rows):
            for j in range(cols):
                if maps[i][j]!='X': start = (i,j); b = True; break
            if b : break

        if b : bfs(start)
    
    answer.sort()
    return answer if answer else [-1]

# from collections import deque
# def solution(maps):
#     answer = []
#     rows, cols = len(maps), len(maps[0])
#     ways = [(1,0), (0,1), (0,-1), (-1,0)]
#     maps = [[i for i in m] for m in maps]
    
#     def bfs(start):
#         queue = deque([start])
#         x,y,v = start
#         first = int(maps[i][j])
#         maps[x][y] = 'X'
#         s = 0
        
#         while queue:
#             x,y,v = queue.popleft()
#             v = int(v)
#             for dx, dy in ways:
#                 nx, ny = x+dx, y+dy
#                 if 0<=nx<rows and 0<=ny<cols and maps[nx][ny]!='X':
#                     s += int(maps[nx][ny])
#                     queue.append((nx,ny,v+int(maps[nx][ny])))
#                     maps[nx][ny] = 'X'
#         answer.append(s+first)
    
    
#     while (rows*cols) != sum(m.count('X') for m in maps):
#         b = False
#         for i in range(rows):
#             for j in range(cols):
#                 if maps[i][j]!='X': start = (i,j,0); b = True; break
#             if b : break

#         if b : dfs(start)
    
    
#     answer.sort()
#     return answer if answer else [-1]





















# # from collections import deque
# # def solution(maps):
# #     # maps.insert(0,'X'*len(maps[0]))
# #     # maps.append('X'*len(maps[0]))
# #     # maps = ['X'+m+'X' for m in maps]
# #     directions = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
# #     rows, cols = len(maps), len(maps[0])
# #     grid = [list(row) for row in maps]
    
# #     def bfs(x, y):
# #         queue = deque([(x, y)])
# #         score = int(grid[x][y])
# #         grid[x][y] = 'X'
        
# #         while queue:
# #             x, y = queue.popleft()
# #             for dx, dy in directions:
# #                 nx, ny = x+dx, y+dy
# #                 if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]!='X':
# #                     queue.append((nx, ny))
# #                     score += int(grid[nx][ny])
# #                     grid[nx][ny] = 'X'
        
# #         return score
    
# #     answer = []
# #     for i in range(rows):
# #         for j in range(cols):
# #             if grid[i][j] != 'X': answer.append(bfs(i,j))
    
    
# #     return sorted(answer) if answer else [-1]