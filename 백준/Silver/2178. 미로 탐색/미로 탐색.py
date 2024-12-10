from collections import deque
def bfs(n, m, maze):
    # 이동 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS를 위한 큐 초기화
    queue = deque()
    queue.append((0, 0))  # 시작 지점 (0, 0) 추가
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        # 목표 지점에 도달하면 거리 반환
        if x == n - 1 and y == m - 1:
            return maze[x][y]
        # 상하좌우 다 둘러보기
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 범위 내에 있고, 벽이 아니며, 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                maze[nx][ny] = maze[x][y] + 1  # 이전 위치에서의 거리 + 1
                queue.append((nx, ny))



n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

print(bfs(n, m, maze))
