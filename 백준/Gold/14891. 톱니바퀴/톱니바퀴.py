def rotation(cogs_list, number, direction, visited):
    if visited[number]:  # 이미 회전한 톱니 바퀴는 무시
        return
    visited[number] = True  # 현재 톱니 바퀴 방문 처리
    
    # 회전 순서도 중요해!! 

    # 왼쪽 톱니바퀴 회전 체크
    if number > 0 and not visited[number - 1]:
        # 왼쪽이 존재하고 방문하지 않았다면
        if cogs_list[number][6] != cogs_list[number - 1][2]:  # 맞물림 체크
            rotation(cogs_list, number - 1, -direction, visited)  # 반대 방향 회전

    # 오른쪽 톱니바퀴 회전 체크
    if number < 3 and not visited[number + 1]:
        # 오른쪽이 존재하고 방문하지 않았다면
        if cogs_list[number][2] != cogs_list[number + 1][6]:  # 맞물림 체크
            rotation(cogs_list, number + 1, -direction, visited)  # 반대 방향 회전

    # 현재 톱니바퀴 회전
    if direction == -1:  # 반시계
        cogs_list[number] = cogs_list[number][1:] + [cogs_list[number][0]]
    else:  # 시계
        cogs_list[number] = [cogs_list[number][-1]] + cogs_list[number][:-1]


cogs_list = []
for _ in range(4):
    cogs = list(map(int, input().strip()))  # 공백 으로 나누어 입력 받지 않는 것 주의
    cogs_list.append(cogs)

k = int(input())

for _ in range(k):
    number, direction = map(int, input().split())
    visited = [False] * 4  # 회전한 톱니바퀴 기록 초기화
    rotation(cogs_list, number - 1, direction, visited)  # 톱니바퀴 번호는 0부터 시작하므로 -1

result = sum((cogs_list[i][0] * (1 << i) for i in range(4)))  # 각 톱니바퀴의 12시 방향 값을 이용하여 점수 계산
print(result)
