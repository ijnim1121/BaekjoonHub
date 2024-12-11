import sys
from collections import deque

input = sys.stdin.read().splitlines()  # 모든 입력을 한꺼번에 받고, 줄 단위로 나눔

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0  # 방문 처리
    count = 1  # 단지 내 집의 수 (시작점 포함)

    # 상, 하, 좌, 우 방향 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 4방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:  # 범위 안에 있는지 확인
                if graph[nx][ny] == 1:  # 집이 있는 경우
                    graph[nx][ny] = 0  # 방문 처리
                    queue.append((nx, ny))
                    count += 1  # 집의 수 추가
    return count


n = int(input[0].strip())  # 첫 번째 줄에 있는 n을 정수로 변환
graph = [list(map(int, list(input[i + 1].strip()))) for i in range(n)]  # n개의 행을 받아 2차원 리스트로 변환


result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:  # 집이 있는 경우
            result.append(bfs(i, j))  # 단지를 BFS로 탐색하여 단지 크기 추가

print(len(result))  # 총 단지 수 출력
for r in sorted(result):  # 오름차순으로 출력
    print(r)
