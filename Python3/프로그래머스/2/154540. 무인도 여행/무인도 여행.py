from collections import deque
def solution(maps):
    # maps.insert(0,'X'*len(maps[0]))
    # maps.append('X'*len(maps[0]))
    # maps = ['X'+m+'X' for m in maps]
    directions = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
    rows, cols = len(maps), len(maps[0])
    grid = [list(row) for row in maps]
    
    def bfs(x, y):
        queue = deque([(x, y)])
        score = int(grid[x][y])
        grid[x][y] = 'X'
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]!='X':
                    queue.append((nx, ny))
                    score += int(grid[nx][ny])
                    grid[nx][ny] = 'X'
        
        return score
    
    answer = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 'X': answer.append(bfs(i,j))
    
    
    return sorted(answer) if answer else [-1]