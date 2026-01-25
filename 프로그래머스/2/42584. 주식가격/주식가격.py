from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    temp = 0
    while(prices):
        temp = prices.popleft()

        day = 0
        for p in prices:
            day += 1
            if temp > p:
                break
               
        temp = 0
        answer.append(day)
    
    return answer