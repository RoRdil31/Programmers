import re
def solution(files):
    answer, new = [], []
    
    for idx, file in enumerate(files):
        head = re.findall(r'[a-z .-]+', file.lower())[0]
        num = re.findall('\d+', file.lower())[0]
        new.append([idx, head, int(num)])
        
    sorted_new = sorted(new, key = lambda x : (x[1], x[2], x[0]))
    index = [l1[0] for l1 in sorted_new]
    
    return [files[i] for i in index]