from collections import deque

# 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
distances = [[-1] * m for _ in range(n)]

# 시작 지점 찾기
start = None
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            start = (i, j)
            distances[i][j] = 0
            break
    if start:
        break

# BFS 초기화
queue = deque([start])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우

# BFS 탐색
while queue:
    x, y = queue.popleft()  # dequeue 에서 가장 앞의 값을 꺼냄
    for dx, dy in directions:
        nx, ny = x + dx, y + dy  # 상하좌우로 이동한 좌표 생성
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and distances[nx][ny] == -1:
            # 범위 내에 있고, 이동할 수 있는지, 아직 방문하지 않았는지
            distances[nx][ny] = distances[x][y] + 1
            # 현재 위치 (x, y)까지의 최단 거리에서 1을 더해 새로운 위치 (nx, ny)까지의 최단 거리를 기록
            queue.append((nx, ny))
            # 새로 방문하게 된 지점 (nx, ny)를 큐에 추가

# 갈 수 없는 곳은 0으로 설정
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            distances[i][j] = 0

# 결과 출력
for row in distances:
    print(" ".join(map(str, row)))
