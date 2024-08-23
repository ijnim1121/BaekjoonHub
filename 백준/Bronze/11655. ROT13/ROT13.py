def rot13(char):
    if 'a' <= char <= 'z':  # 소문자일 경우
        return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
    # ord함수는 주어진 문자의 아스키 값을 반환
    # ord(char) - ord('a'): 입력된 문자의 위치를 알파벳 시작인 'a'를 기준으로 계산
    # +13: 13글자 밀어서 변환
    # %26: 알파벳의 범위를 유지하기 위해 26으로 나눈 나머지 계산
        # 만약 'z'에 대해 계산한다면:
        # ord('z') - ord('a') + 13는 25 + 13 = 38이므로,
        # 38 % 26 = 12가 되어 'm'으로 변환
    # + ord('a'): 최종적으로 구한 인덱스 값에 알파벳의 시작인 'a'를 다시 더해 최종적으로 변환된 문자의 아스키 값을 구하고
    #chr()로 아스키 값 -> 문자로 변환

    elif 'A' <= char <= 'Z':  # 대문자일 경우
        return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
    else:
        return char  # 알파벳이 아닐 경우 그대로 반환

# 문자열 입력 받기
S = input()

# ROT13 적용
rot13_result = ''.join(rot13(char) for char in S)
# ROT13방식으로 변환된 문자들을 하나의 문자열로 결합하는 과정
# join() 메서드는 문자열의 리스트나 제너레이터를 하나의 문자열로 결합하는 데 사용

print(rot13_result)