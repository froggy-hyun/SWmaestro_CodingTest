def solution(progresses, speeds):
    answer = []
    while(progresses):
        # 작업 수행
        for i in range(len(progresses)):
            if(progresses[i] < 100):
                progresses[i] += speeds[i]
        
        # 배포 가능 여부 체크 및 배포
        release = 0
        while(len(progresses) != 0):
            if(progresses[0] >= 100):
                progresses.remove(progresses[0])
                speeds.remove(speeds[0])
                release += 1
            else:
                break
        if(release != 0):
            answer.append(release)
    return answer