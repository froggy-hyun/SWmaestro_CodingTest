def solution(nums):
    capability = len(nums) / 2
    nums = set(nums)
    if len(nums) <= capability:
        return len(nums)
    else:
        return capability
