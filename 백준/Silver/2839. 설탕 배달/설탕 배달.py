def sugar_delivery_dp(N):
    # 0으로 초기화 하면 0개로 판단 하게 되어 (만들 수 없는 무게 = 무한 대)로 초기화
    dp = [float('inf')] * (N + 1)

    # 3kg, 5kg 봉지를 사용할 수 있는 기본 무게에 대한 최소값 설정
    if N >= 3: # N이 3보다 작으면 dp[3]에 접근할 수 없음 => 해당 구문 생략하면 런타임 에러
        dp[3] = 1
    if N >= 5:
        dp[5] = 1

    # DP로 모든 무게에 대해 최소 봉지 개수 계산
    for i in range(6, N + 1):
        if dp[i - 3] != float('inf'): # i-3 kg 을 만들 수 있어야 3kg 봉지를 사용할 수 있음
            dp[i] = min(dp[i], dp[i - 3] + 1)
        if dp[i - 5] != float('inf'):
            dp[i] = min(dp[i], dp[i - 5] + 1)

    # N 킬로그램을 만들 수 없다면 -1 출력, 그렇지 않으면 최소 봉지 수 출력
    if dp[N] == float('inf'):
        return -1
    else:
        return dp[N]

# 입력 받기
N = int(input())
print(sugar_delivery_dp(N))
