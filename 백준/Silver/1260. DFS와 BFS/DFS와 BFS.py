from collections import deque

# 정점의 개수, 간선의 개수, 탐색 시작 번호
N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited_dfs = [False for _ in range(N + 1)]
visited_bfs = [False for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# 방문할 수 있는 정점이 여러개인 경우에는 정점 번호가 작은 것을 먼저 방문한다했으므로
for row in graph:
    row.sort()
# 스택
def dfs(graph, V, visited_dfs):
    visited_dfs[V] = True
    print(V, end=' ')
    for v in graph[V]:
        if not visited_dfs[v]:
            dfs(graph, v, visited_dfs)

# 큐
def bfs(graph, V, visited_bfs):
    queue = deque([V])
    visited_bfs[V] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)