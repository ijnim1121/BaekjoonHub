def is_valid_password(password):
    vowels = 'aeiou'
    has_vowel = False
    prev_char = ''
    consecutive_count = 1
    vowel_count = 0
    consonant_count = 0
    is_acceptable = True

    for i in range(len(password)):
        if password[i] in vowels:
            has_vowel = True
            vowel_count += 1
            consonant_count = 0  # 자음 카운트 초기화
        else:
            vowel_count = 0  # 모음 카운트 초기화
            consonant_count += 1

        # 같은 글자가 연속으로 두 번 오는지 체크
        if password[i] == prev_char:
            consecutive_count += 1
            if consecutive_count >= 2 and password[i] not in ['e', 'o']:
                is_acceptable = False
        else:
            consecutive_count = 1  # 연속 문자 카운트 초기화


        # 모음이 3개 연속으로 오는지 체크
        if vowel_count > 2:
            is_acceptable = False

        # 자음이 3개 연속으로 오는지 체크
        if consonant_count > 2:
            is_acceptable = False

        prev_char = password[i]  # 이전 문자 업데이트

    return has_vowel and is_acceptable

while True:
    password = input()
    if password == "end":
        break
    if is_valid_password(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")