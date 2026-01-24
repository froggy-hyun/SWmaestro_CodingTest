def solution(arr):
    result = []
    for c in arr:
        if len(result) == 0 or result[-1] != c:
            result.append(c)

    return result