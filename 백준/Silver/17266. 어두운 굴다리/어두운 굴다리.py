import math
# 굴다리 길이
N = int(input())
# 가로등 개수
M = int(input())
# 가로등 위치
x = list(map(int, input().split()))

def light_height(N,M,x):
    # 가로등이 1개라면, max(가로등위치 - 0, 굴다리길이 - 가로등위치)
    if M == 1:
        height = max(x[0]-0, N-x[0])
        return height
    # 가로등이 2개 이상이라면, 가로등간의 간격들과 첫값과 끝값 비교 중 최대값 = 가로등 높이
    else:
        # 가로등 간 간격에서 가장 큰 값 찾기
        max_gap = 0
        for i in range(M - 1):
            max_gap = max(max_gap, x[i + 1] - x[i])

        # 첫 번째 가로등과 시작점, 마지막 가로등과 끝점 간의 거리도 고려
        height = max(math.ceil(max_gap / 2), x[0] - 0, N - x[-1])
        return height

print(light_height(N,M,x))