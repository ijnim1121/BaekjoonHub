# 테스트 케이스의 개수 T 입력
T = int(input())

def pick(A, n):
    sortedA = sorted(A, reverse=True)
    return sortedA[n - 1]

for _ in range(T):
    # 배열 A의 원소 10개 입력
    A = list(map(int, input().split()))

    # 원하는 인덱스 (예: 3번째 큰 수)
    result = pick(A, 3)

    # 결과 출력
    print(result)

