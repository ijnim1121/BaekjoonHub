def solution(n):
    list_string = list(str(n))
    list_string.sort(reverse=True)
    answer = int("".join(list_string))
    return answer