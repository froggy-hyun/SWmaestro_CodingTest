def solution(clothes):
    answer = 1
    clothes_type = dict()
    for cloth, cloth_type in clothes:
        if cloth_type not in clothes_type:
            clothes_type[cloth_type] = 2
        else:
            clothes_type[cloth_type] += 1
    for count in clothes_type.values():
        answer *= count
    
    answer -= 1
    return answer