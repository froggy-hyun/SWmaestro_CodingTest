def solution(prices):
    answer = []
    for i in range(len(prices)):
        duration = 0
        for j in range(i+1, len(prices)):
            duration += 1
            if (prices[i] > prices[j]):
                break
        answer.append(duration)
        
    return answer