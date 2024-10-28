from functools import cmp_to_key

def solution(numbers):
    # numbers의 각 요소를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 커스텀 정렬 기준을 정의하여 정렬
    numbers.sort(key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))
    
    # 정렬된 결과를 이어 붙여 결과 반환
    answer = ''.join(numbers)
    
    # 예외 처리: 결과가 '0'으로만 이루어진 경우 '0' 반환
    return answer if answer[0] != '0' else '0'
