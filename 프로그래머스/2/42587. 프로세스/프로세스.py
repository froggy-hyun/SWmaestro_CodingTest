def solution(priorities, location):
    answer = 0
    while priorities[location] != 0:
        for i in range(len(priorities)):
            if priorities[i] == max(priorities):
                priorities[i] = 0
                answer += 1
            if priorities[location] == 0:
                break
                
    return answer