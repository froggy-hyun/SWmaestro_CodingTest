#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    nums, ex_count = input().split()
    ex_count = int(ex_count)

    state = {nums}

    for _ in range(ex_count):
        next_state = set()

        for s in state:
            for i in range(len(nums) - 1):
                for j in range(i+1, len(nums)):
                    digits = list(s)
                    digits[i], digits[j] = digits[j], digits[i]
                    d = ''.join(digits)

                    if d not in next_state:
                        next_state.add(d)

        state = next_state

    print("#%d %s" %(test_case, max(state)))