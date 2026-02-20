def solution(n, lost, reserve):
    
    answer = n
    
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))
    
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] in (reserve[j] - 1, reserve[j] + 1):
                lost[i] = -1
                reserve[j] = -1
                
    for l in lost:
        if l != -1:
            answer -= 1

    return answer