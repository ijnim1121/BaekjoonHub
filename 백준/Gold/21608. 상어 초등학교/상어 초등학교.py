n = int(input())
students = {}
order = []  # 자리 배치 순서
for _ in range(n * n):
    data = list(map(int, input().split()))
    students[data[0]] = data[1:]
    order.append(data[0])

# 방향 벡터: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기 교실 (n x n 크기)
classroom = [[0] * n for _ in range(n)]

# 학생 배치 함수
def place_student(student):
    max_like, max_empty, best_pos = -1, -1, None
    # max_like: 현재까지 찾은 자리 중에서 가장 많은 선호하는 친구가 인접해 있는 자리의 친구 수
    # max_empty: 인접한 칸 중에서 비어있는 칸의 최대 개수
    # best_pos: 조건에 맞는 최적의 자리를 (행,열) 형태의 튜플로 저장
    for x in range(n):
        for y in range(n):
            if classroom[x][y] == 0:  # 비어있는 자리만 확인
                like_count, empty_count = 0, 0 # 현재자리x,y에 인접한 칸 중 선호하는 친구의수와 비어있는 칸의 수
                for d in range(4): # 상하좌우 탐색
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if classroom[nx][ny] in students[student]: #선호하는 친구가 앉아있다면
                            like_count += 1
                        elif classroom[nx][ny] == 0: # 자리가 비어있다면
                            empty_count += 1
                # 조건에 맞는 자리 찾기
                if (like_count > max_like or # 선호하는 친구가 더 많으면 자리 갱신
                    (like_count == max_like and empty_count > max_empty) or # 비어있는 칸이 더 많으면 자리 갱신
                    (like_count == max_like and empty_count == max_empty and (x, y) < best_pos)):
                    # like_count와 empty_count가 모두 같다면 x,y가 best_pos보다 앞에 있는 자리로 갱신
                    max_like, max_empty, best_pos = like_count, empty_count, (x, y)
    # best_pos가 결정되면, 해당 위치에 현재 학생을 배치
    classroom[best_pos[0]][best_pos[1]] = student

# 모든 학생 배치
for student in order:
    place_student(student)

# 만족도 계산 함수
def calculate_satisfaction():
    satisfaction = 0
    for x in range(n): # 교실 순회
        for y in range(n):
            student = classroom[x][y]
            like_count = 0
            for d in range(4): # 상하좌우 인접 칸 탐색
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if classroom[nx][ny] in students[student]:
                        like_count += 1
            # 만족도 점수 계산
            if like_count > 0:
                satisfaction += 10 ** (like_count - 1)
            #like_count가 1이면 만족도 점수는 10^0=1, 2이면 10^1=10 .....
    return satisfaction

# 최종 만족도 출력
print(calculate_satisfaction())
