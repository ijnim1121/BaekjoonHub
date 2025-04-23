def solution(numbers):
    list = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            list.append(numbers[i] + numbers[j])
    answer = sorted(set(list))
    return answer