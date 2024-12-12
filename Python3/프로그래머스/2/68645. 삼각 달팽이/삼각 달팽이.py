from itertools import chain
def solution(n):
    ans = [[0]*(i+1) for i in range(n)]
    num, y, x = 1, 0, 0
    last = n*(n+1)//2
    if n==1 : return [1]
    
    for i in range(n):
        
        while y < n and ans[y][x] == 0: # down
            ans[y][x] = num
            if num == last : return list(chain(*ans))
            y += 1
            num += 1
        y, x = y-1, x+1
        
        while x < n and ans[y][x] == 0: # right
            ans[y][x] = num
            if num == last : return list(chain(*ans))
            x += 1
            num += 1
        x, y = x-2, y-1
        
        while x >= 0 and y >= 0 and ans[y][x] == 0: # up
            ans[y][x] = num
            if num == last : return list(chain(*ans))
            x, y = x-1, y-1
            num += 1
        x, y = x+1, y+2
            
    return list(chain(*ans))
