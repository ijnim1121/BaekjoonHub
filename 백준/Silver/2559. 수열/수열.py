N, K = map(int, input().split())
temp = list(map(int, input().split()))

def temp_range_sum(N, K, temp):
    # 초기 K일의 합 계산
    current_sum = sum(temp[:K])
    max_sum = current_sum

    # 슬라이딩 윈도우로 최대 합 계산
    for i in range(K,N):
        current_sum = current_sum + temp[i] - temp[i-K]
        max_sum = max(max_sum,current_sum)

    return max_sum

print(temp_range_sum(N,K,temp))