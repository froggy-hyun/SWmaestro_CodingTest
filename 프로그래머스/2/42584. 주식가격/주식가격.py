from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    while(prices):
        temp = prices.popleft()

        day = 0
        for p in prices:
            day += 1
            if temp > p:
                break
              
        answer.append(day)
    
    return answer