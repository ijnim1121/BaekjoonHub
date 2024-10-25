from itertools import combinations

def chicken_distance(m, houses, chickens):
    # M개의 치킨집 조합 선택
    min_distance = float('inf')
    for selected_chickens in combinations(chickens,m):
        total_distance = 0
        # 각 집에 대해 가장 가까운 치킨집 거리 찾기
        for hx, hy in houses:
            distance = min(abs(hx - cx) + abs(hy - cy) for cx, cy in selected_chickens)
            total_distance += distance
        # 최소 치킨 거리 갱신
        min_distance = min(min_distance,total_distance)
    return min_distance

# 입력 구현
n,m = map(int,input().split())
city_info = []
for _ in range(n):
    city_info.append(list(map(int,input().split())))

# 집과 치킨집 위치 리스트
houses = []
chickens = []

# 1 = 집, 2 = 치킨집
for i in range(n):
    for j in range(n):
        if city_info[i][j] == 1:
            houses.append([i,j])
        elif city_info[i][j] == 2:
            chickens.append([i,j])

print(chicken_distance(m, houses, chickens))