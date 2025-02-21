from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    bridge_weight = 0 
    while(truck_weights):
        answer += 1
        bridge_weight -= bridge.popleft()
        # bridge_weight = sum(bridge)
        
        
        if (weight >= bridge_weight + truck_weights[0]): #sum함수에서 시간초과가 나니, 변수 설정
            
            pop = truck_weights.popleft()
            bridge_weight += pop
            bridge.append(pop)
        else:
            bridge.append(0)
    
    answer += bridge_length
    
    return answer


