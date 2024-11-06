n = int(input())
consulting = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

for i in range(n):
    time, pay = consulting[i]
    # 현재 날짜까지의 최대 수익
    dp[i + 1] = max(dp[i + 1], dp[i])
    # 상담을 진행했을 경우 종료일에 수익을 반영
    if i + time <= n:
        dp[i + time] = max(dp[i + time], dp[i] + pay)

print(dp[n])
