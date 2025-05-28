def solution(nums):
    answer = 0
    possible_max = len(nums) // 2
    ponketmon = set(nums)
    if possible_max <  len(ponketmon):
        answer = possible_max
    else:
        answer = len(ponketmon)
    
    return answer