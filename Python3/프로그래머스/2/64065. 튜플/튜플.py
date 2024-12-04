import re
from collections import Counter
def solution(s):
    s = Counter(re.findall('\d+', s))
    return [int(v) for v, cnt in s.most_common()]
    