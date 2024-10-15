t = int(input())  # 테스트 케이스 수
for _ in range(t):
    passwords = input()

    left_stack = []  # 커서 왼쪽에 있는 문자들을 저장하는 스택
    right_stack = []  # 커서 오른쪽에 있는 문자들을 저장하는 스택

    for password in passwords:
        if password == '<':  # 커서를 왼쪽으로 이동
            if left_stack:
                right_stack.append(left_stack.pop())  # 왼쪽 스택에서 오른쪽 스택으로 이동
        elif password == '>':  # 커서를 오른쪽으로 이동
            if right_stack:
                left_stack.append(right_stack.pop())  # 오른쪽 스택에서 왼쪽 스택으로 이동
        elif password == '-':  # 백스페이스, 커서 왼쪽 문자 삭제
            if left_stack:
                left_stack.pop()  # 왼쪽 스택에서 삭제
        else:  # 문자 입력
            left_stack.append(password)  # 왼쪽 스택에 문자 추가

    # 최종 결과는 왼쪽 스택 + 오른쪽 스택 (오른쪽 스택은 역순으로 처리)
    result = ''.join(left_stack + right_stack[::-1])
    print(result)
