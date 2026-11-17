#import sys
#sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())

    building_heights = list(map(int, input().split()))

    result = 0

    for i in range(2, N-2):
        tallest_building = max(building_heights[i-2], building_heights[i-1], building_heights[i+1], building_heights[i+2])
        view = building_heights[i] - tallest_building

        if view > 0:
            result += view


    print("#%d %d" %(test_case, result))