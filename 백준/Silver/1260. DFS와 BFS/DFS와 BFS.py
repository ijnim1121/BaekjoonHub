from collections import deque
N,M,V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited_dfs = [False for _ in range(N+1)]
visited_bfs = [False for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for row in graph:
    row.sort()
def dfs(graph, V, visited_dfs):
    visited_dfs[V] = True
    print(V, end=' ')
    for v in graph[V]:
        if not visited_dfs[v]:
            dfs(graph, v, visited_dfs)
def bfs(graph, V, visited_bfs):
    queue = deque([V])
    visited_bfs[V] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i]= True
dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)