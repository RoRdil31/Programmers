from collections import Counter
def solution(dirs):
    answer, now, paths = 0, [0,0], [[0,0]]
    ways = {'U':[0,1], 'D':[0,-1], 'L':[-1,0], 'R':[1,0]}
    for i in dirs:
        nxt = list(map(sum, zip(now, ways[i])))
        if ((-5 <= nxt[0] <= 5) and (-5 <= nxt[1] <= 5)):
            now = nxt
            paths.append(now)
    print(paths)
    two = []
    for i in range(len(paths)-1):
        s1 = f'{paths[i][0]}{paths[i][1]}{paths[i+1][0]}{paths[i+1][1]}'
        s2 = f'{paths[i+1][0]}{paths[i+1][1]}{paths[i][0]}{paths[i][1]}'
        print(s1, s2)
        if (s1 in two) or (s2 in two):
            continue
        two.append(s1)
    return len(two)
    
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