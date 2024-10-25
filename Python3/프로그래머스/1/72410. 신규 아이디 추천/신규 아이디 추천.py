import re
def solution(new_id):
    # 1,2단계 : 소문자, 숫자, '.', '_', '-' 만 추출.
    new_id = ''.join(re.findall(r'[a-z0-9._-]', new_id.lower()))
    
    # 3단계 : 마침표 2번 이상 연속 -> 1개로.
    new_id = re.sub(r'\.+','.', new_id)
    
    # 4단계 : 마침표 처음이나 끝에 있으면 제거.
    new_id = new_id.strip('.')
    
    # 5단계 : 빈 문자열이라면, "a" 대입.
    if not new_id : new_id = "a"
    
    # 6단계 : 길이 >= 16, 제거 후 끝에 마침표 있다면 제거.
    if len(new_id) >= 16 : new_id = new_id[:15].strip('.')
    
    # 7단계 : 길이 <= 2, 길이 3 될 때까지 마지막 문자 붙임.
    if len(new_id) <= 2 : 
        new_id += new_id[-1]*(3-len(new_id))
    
    return new_id