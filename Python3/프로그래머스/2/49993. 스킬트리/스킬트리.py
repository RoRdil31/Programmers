def solution(skill, skill_trees):
    answer, cnt = [], 0
    trees = [''.join([w for w in tree if w in skill]) for tree in skill_trees]
    for tree in trees:
        if tree == '' : cnt += 1; continue
        if (tree[0]==skill[0]) and (tree in skill) : cnt += 1
    # print(trees)
    return cnt