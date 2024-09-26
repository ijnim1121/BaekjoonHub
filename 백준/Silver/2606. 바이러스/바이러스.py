from collections import deque

# BFS
def wormVirus(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 웜 바이러스에 걸리게 되는 컴퓨터의 수
    count = 0
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft() # 큐에서 가장왼쪽에 있는 요소
        for i in graph[v]: # v=1이라면 i는 graph[1]에 있는 요소들 [2,5]
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    print(count)

# 컴퓨터의 수
N = int(input())
# 네트워크 상 연결된 쌍의 수
M = int(input())
# 컴퓨터간 연결을 저장할 그래프
graph = [[] for _ in range(N+1)]
# 리스트의 인덱스는 0부터 시작하지만, 컴퓨터의 번호가 1부터 이므로 graph[0]은 사용하지 않고
# graph[1] 부터 graph[N]까지 사용하기 위해 N+1로 범위 설정

# 각 노드가 방문된 정보를 표현하는 리스트
visited = [False] * (N+1)

# 네트워크 연결 정보 입력 받기
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

wormVirus(graph, 1, visited)