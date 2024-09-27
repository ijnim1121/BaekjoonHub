# 변수명 및 함수명: 스네이크 케이스 사용 (예: my_variable, calculate_sum)
# 클래스명: 파스칼 케이스(Pascal Case, 또는 카멜 케이스) 사용 (예: MyClass, PersonManager)
# 상수: 모두 대문자와 언더스코어로 구분 (예: MAX_LIMIT, DEFAULT_TIMEOUT)

# DFS
def number_of_relations(graph, start, find, visited, cnt):
        visited[start] = True # 현재 노드 방문처리

        # 찾으려는 노드를 발견했을 때, 경로의 길이를 출력하고 종료
        if start == find:
            print(cnt)
            exit()
        for i in graph[start]:
            if visited[i] == False: # 아직 방문하지않은 노드에 대해
                visited[i] = True # 방문처리
                number_of_relations(graph,i,find, visited, cnt+1) #재귀적 탐색

# 전체 사람의 수
n = int(input())
# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
p1, p2 = map(int, input().split())
# 부모 자식들 간의 관계의 개수
m = int(input())
# 부모 자식들 간의 관계를 나타 내는 두 번호 x(부모),y(자식)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 각 노드가 방문된 정보를 표현
visited = [False] * (n+1)

cnt = 0
# 정의된 함수 호출
number_of_relations(graph,p1,p2,visited,cnt)

# 만약 함수가 끝났는데도 exit()로 프로그램이 종료되지 않았다면 경로를 찾지 못한 것
print(-1)
