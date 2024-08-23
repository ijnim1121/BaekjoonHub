from collections import Counter
def most_common_letter(word):
    # 대문자와 소문자를 구분하지 않기 위해 모두 대문자로 변환
    word = word.upper()

    # 알파벳의 빈도수 계산
    letter_counts = Counter(word)
    # ex) Counter("hello")는 {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    # 가장 많이 사용된 알파벳과 그 빈도수 찾기
    max_count = max(letter_counts.values())
    # 예를 들어, Counter 객체가 {'a': 3, 'b': 2}일 경우, letter_counts.values()는 dict_values([3, 2])를 반환
    most_common_letters = [letter for letter, count in letter_counts.items() if count == max_count]
    # items() 메서드는 이 객체의 키 - 값쌍을 튜플 형태로 반환
    # 예를들어, Counter({'a': 3, 'b': 2, 'c': 1}) 일 경우,
    # letter_counts.items()는 dict_items([('a', 3), ('b', 2), ('c', 1)])를 반환

    # for letter, count in letter_counts.items()는 letter_counts의 각 키-값 쌍을 순회
    # 여기서 letter는 키(문자), count는 그 문자의 빈도수

    # 결과 출력
    if len(most_common_letters) > 1:
        return '?'
    else:
        return most_common_letters[0]

# 입력 받기
input_word = input().strip()
result = most_common_letter(input_word)
print(result)
