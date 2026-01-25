from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    finish = []
    bridge = [0 for _ in range(bridge_length - 1)]
    count = len(truck_weights)
    while (len(finish) != count):
        answer += 1
        if(truck_weights and sum(bridge) + truck_weights[0] <= weight):
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
        
        car = bridge.pop(0)
        if car != 0:
            finish.append(car)
            
    return answer