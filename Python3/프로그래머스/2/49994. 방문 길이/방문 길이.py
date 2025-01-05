def solution(dirs):
    cnt = 0
    x, y, visited = 0, 0, []
    ways = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    for i in dirs:
        nx, ny = x+ways[i][0], y+ways[i][1]
        if (-5<=nx<=5) and (-5<=ny<=5):
            if (x,nx,y,ny) not in visited:
                cnt += 1
                visited.append((x,nx,y,ny))
                visited.append((nx,x,ny,y))
            x, y = nx, ny
        
    return cnt




















# def solution(dirs):
#     x, y, paths = 0, 0, set()
#     ways = {'U':[0,1], 'D':[0,-1], 'L':[-1,0], 'R':[1,0]}
#     for i in dirs:
#         dx = x + ways[i][0]
#         dy = y + ways[i][1]
#         if ((-5 <= dx <= 5) and (-5 <= dy <= 5)):
#             paths.add((x,y,dx,dy))
#             paths.add((dx,dy,x,y))
#             x, y = dx, dy
#     return len(paths)//2
