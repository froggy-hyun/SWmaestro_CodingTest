#import sys
#sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dump_count = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump_count):
        highest = max(boxes)
        lowest = min(boxes)

        if highest - lowest <= 1:
            break

        boxes[boxes.index(highest)] -= 1
        boxes[boxes.index(lowest)] += 1
        
    print("#%d %d" %(test_case, max(boxes)-min(boxes)))
