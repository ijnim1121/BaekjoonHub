N, K = map(int, input().split())
items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

# DP 배열 초기화 /  배낭의 무게를 0부터 최대 K까지 모두 표현
dp = [0] * (K + 1)

# DP 배열 채우기
for W, V in items:  # items 리스트에 들어 있는 각 아이템 (W, V)을 하나씩 순회
    for weight in range(K, W - 1, -1):  # 무게 한도 K부터 아이템의 무게 W까지 탐색
        dp[weight] = max(dp[weight], dp[weight - W] + V)
        # ex) 배낭의 현재 무게가 7, 현재 아이템의 무게가 3이라면 dp[7 - 3] = dp[4]
        # 즉, dp[weight - W] => 무게가 4일 때 배낭에 넣을 수 있는 최대 가치를 의미
        # V => 현재 아이템의 가치

# 최종적으로 dp[K] 값,  배낭의 최대 무게가 K일 때 얻을 수 있는 최대 가치
print(dp[K])


