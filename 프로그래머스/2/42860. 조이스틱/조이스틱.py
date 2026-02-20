def solution(name):
    answer = 0
    
    for i,s in enumerate(name):
        if name[i:].count('A') == len(name[i:]):
            break
        if ord(s) - ord('A') < ord('Z') - ord(s) + 1 : 
            answer += (ord(s) - ord('A'))
        else:
            answer += (ord('Z') - ord(s) + 1)
    
    move = len(name) - 1
    for idx in range(len(name)):
        next_idx = idx + 1
        while(next_idx < len(name) and name[next_idx] == 'A'):
            next_idx += 1
        dup_move = min(idx, len(name) - next_idx)
        move = min(move, idx + len(name) - next_idx + dup_move)
        
    answer += move
            
    return answer