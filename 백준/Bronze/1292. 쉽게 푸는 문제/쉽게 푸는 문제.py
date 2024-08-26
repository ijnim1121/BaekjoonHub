def generate_sequence(n):
    sequence = []
    for i in range(1, n + 1):
        sequence.extend([i] * i)  # i를 i번 추가
    # for i in range(1, n + 1):
    #     for _ in range(i):  # i번 반복하여 추가
    #         sequence.append(i)  # i를 추가
    return sequence

# extend 사용: sequence.extend([i] * i)는 i라는 숫자를 i번 리스트로 만들어서 한 번에 추가, 결과적으로 같은 숫자가 연속적으로 나열됨.
# append 사용: sequence.append(i)는 i를 하나씩 추가, 이를 위해 for _ in range(i)를 사용하여 i번 반복.
    
# 입력 받기
A, B = map(int, input().split())

# 수열의 최대 길이 계산
max_length = B  # B는 최대 1000이므로 1000만큼의 수열 생성

# 수열 생성
sequence = generate_sequence(max_length)

# 구간 A번째부터 B번째까지의 합 계산 (인덱스는 0부터 시작하므로 A-1, B)
result = sum(sequence[A-1:B])

# 결과 출력
print(result)


# append 사용 시 리스트에 추가된 요소는 하나의 요소로 인식됩니다.
# extend 사용 시 리스트에 추가된 요소들은 개별적으로 리스트에 추가됩니다.
# lst = [1, 2, 3]

# append 예시
# lst.append([4, 5])
# print(lst)  # 출력: [1, 2, 3, [4, 5]]

# 초기화
# lst = [1, 2, 3]

# extend 예시
# lst.extend([4, 5])
# print(lst)  # 출력: [1, 2, 3, 4, 5]

