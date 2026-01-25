import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
   
    answer = 0

    while(len(scoville) >= 2):
        
        minK = heapq.heappop(scoville)
        if minK >= K:
            return answer
        else:
            heapq.heappush(scoville, minK)
            
        answer += 1
        heapq.heappush(scoville, (heapq.heappop(scoville) + heapq.heappop(scoville)*2))
        
    if scoville[0] >= K:
        return answer
    else:
        return -1