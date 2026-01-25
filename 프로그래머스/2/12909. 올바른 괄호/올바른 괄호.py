def solution(s):
    answer = True
    
    stack = []
    
    try:
        for c in s:
            if c == '(':
                stack.append('(')
            else:
                stack.pop()
    except:
        return False
    
    if stack:
        return False

    return True