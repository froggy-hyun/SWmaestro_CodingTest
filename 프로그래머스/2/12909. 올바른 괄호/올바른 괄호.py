def solution(s):
    answer = False
    
    left = 0
    right = 0
    for c in s:
        if c == '(':
            left += 1
        else:
            right += 1
        if (right > left):
            return False
        
    if (s[0] == '(' and s[-1] == ')' and left == right):
        answer = True   
    
    return answer
