#import sys
#sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())

    building_heights = list(map(int, input().split()))

    result = 0

    def compare(b_index, comp_index):
        left_count = building_heights[b_index] - building_heights[comp_index]
        return left_count

    for i in range(2, N-2):
        if i == 2:
            count = min(compare(i, i+1), compare(i, i+2))
            if count > 0:
                result += count
        elif i == N-2:
            count = min(compare(i, i - 1), compare(i, i - 2))
            if count > 0:
                result += count
        else:
            count = min(compare(i, i + 1), compare(i, i + 2), compare(i, i - 1), compare(i, i - 2))
            if count > 0:
                result += count

    print("#%d %d" %(test_case, result))