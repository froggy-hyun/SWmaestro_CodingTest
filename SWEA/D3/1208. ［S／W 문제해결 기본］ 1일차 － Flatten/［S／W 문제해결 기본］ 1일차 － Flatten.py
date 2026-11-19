#import sys
#sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dump_count = int(input())

    boxes = list(map(int, input().split()))

    while(dump_count != 0):
        boxes[boxes.index(max(boxes))] -= 1
        dump_count -= 1
        boxes[boxes.index(min(boxes))] += 1
    print("#%d %d" %(test_case, max(boxes)-min(boxes)))

