def solution(dirs):
    x, y, paths = 0, 0, set()
    ways = {'U':[0,1], 'D':[0,-1], 'L':[-1,0], 'R':[1,0]}
    for i in dirs:
        # nxt = list(map(sum, zip(now, ways[i])))
        dx = x + ways[i][0]
        dy = y + ways[i][1]
        if ((-5 <= dx <= 5) and (-5 <= dy <= 5)):
            paths.add((x,y,dx,dy))
            paths.add((dx,dy,x,y))
            
            x, y = dx, dy
    print(paths)
    # two = []
    # for i in range(len(paths)-1):
    #     s1 = f'{paths[i][0]}{paths[i][1]}{paths[i+1][0]}{paths[i+1][1]}'
    #     s2 = f'{paths[i+1][0]}{paths[i+1][1]}{paths[i][0]}{paths[i][1]}'
    #     print(s1, s2)
    #     if (s1 in two) or (s2 in two):
    #         continue
    #     two.append(s1)
    return len(paths)//2
    
    # two_paths = [f'{paths[i][0]}{paths[i][1]}{paths[i+1][0]}{paths[i+1][1]}' for i in range(len(paths)-1)]
    # two_paths2 = [f'{paths[i+1][0]}{paths[i+1][1]}{paths[i][0]}{paths[i][1]}' for i in range(len(paths)-1)]
    # two_paths.extend(two_paths2)
    
# #     print(len(paths), paths)
# #     print(len(two_paths), two_paths)
# #     print(len(set(two_paths)), set(two_paths))
    
#     two_paths = Counter(two_paths)
#     print(paths)
#     print(two_paths)
#     print(len(two_paths)//2)
    
#     # minus = 0
#     # for idx, value in two_paths.most_common()[::2]:
#     #     minus += value-1
#     minus = False
#     for i in two_paths.values():
#         if i >= 4 : minus=True; break
        
#     return len(two_paths)//2 + 1 - minus