import sys
from collections import deque

input = sys.stdin.readline

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

# A번 도시에서 B번 도시로 이동하는 M개의 단방향 도로를 저장
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)


# BFS 탐색
def bfs(start):
    # 각 도시 까지의 거리를 저장 하는 리스트 (-1로 초기화)
    distance = [-1] * (N + 1)
    distance[start] = 0  # 시작 도시의 거리는 0

    queue = deque([start])

    while queue:
        current = queue.popleft()

        # 현재 도시와 연결된 다른 도시들을 확인
        for next_city in graph[current]:
            if distance[next_city] == -1:  # 아직 방문하지 않은 도시일 경우
                distance[next_city] = distance[current] + 1
                queue.append(next_city)

    # 최단 거리가 K인 도시들을 출력
    result = []
    for city in range(1, N + 1):
        if distance[city] == K:
            result.append(city)

    # 결과가 있을 경우 도시 번호를 출력하고, 없을 경우 -1 출력
    if result:
        for city in result:
            print(city)
    else:
        print(-1)


bfs(X)