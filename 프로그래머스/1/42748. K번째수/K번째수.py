def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sliced_array = array[i-1:j]  # i번째부터 j번째까지 자른 배열
        sorted_array = sorted(sliced_array)  # 정렬된 배열
        answer.append(sorted_array[k-1])  # k번째 원소 추가
    return answer
