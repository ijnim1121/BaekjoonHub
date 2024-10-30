import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
tables = []

for _ in range(N):
    table = list(map(int, input().split()))
    tables.append(table)

# 2차원 dp 배열 생성 및 누적합 계산
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = tables[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

# 구간합 계산 함수
def range_sum(x1, y1, x2, y2):
    result = dp[x2][y2]
    if x1 > 1:
        result -= dp[x1 - 1][y2]
    if y1 > 1:
        result -= dp[x2][y1 - 1]
    if x1 > 1 and y1 > 1:
        result += dp[x1 - 1][y1 - 1]
    return result

sum_list = []
# 쿼리 처리 및 출력
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    sum = range_sum(x1, y1, x2, y2)
    sum_list.append(sum)


for result in sum_list:
    print(result)
