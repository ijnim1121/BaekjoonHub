def backtrack(i, current_value):
    global max_result, min_result, add, sub, mul, div

    # 숫자의 끝까지 연산을 했을 경우
    if i == n:
        max_result = max(max_result, current_value)
        min_result = min(min_result, current_value)
        return #현재 경로의 탐색을 종료

    # 각 연산자가 남아있을 때 백트래킹을 사용해 연산 수행
    if add > 0:
        add -= 1
        backtrack(i + 1, current_value + numbers[i])
        add += 1

    if sub > 0:
        sub -= 1
        backtrack(i + 1, current_value - numbers[i])
        sub += 1

    if mul > 0:
        mul -= 1
        backtrack(i + 1, current_value * numbers[i])
        mul += 1

    if div > 0:
        div -= 1
        # 나눗셈에서 음수 처리
        if current_value < 0:
            backtrack(i + 1, -(-current_value // numbers[i]))
        else:
            backtrack(i + 1, current_value // numbers[i])
        div += 1


n = int(input())  # 숫자의 개수
numbers = list(map(int, input().split()))  # 숫자 리스트
add, sub, mul, div = map(int, input().split())  # 연산자의 개수

# 결과값 초기화
max_result = -float('inf')
min_result = float('inf')

# 백트래킹 시작
backtrack(1, numbers[0])

# 결과 출력
print(max_result)
print(min_result)
