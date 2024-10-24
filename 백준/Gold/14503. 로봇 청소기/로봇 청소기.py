def robot_clean(N,M,r,c,d,status_list,cleaned_count):
    # 북, 동, 남, 서 방향 정의
    # ex) 북 쪽으로 가면 위로 한칸, 좌표상 x축이 하나 줄어듦 = (-1,0)
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    while True:
        if status_list[r][c] == 0:
            status_list[r][c] = -1 #청소된 위치 = -1
            cleaned_count += 1

        # 4방향 모두 확인
        # 청소되지 않은 경우
        cleaned = False
        for _ in range(4):
            # 반시계 방향 90도 회전
            d = turn_left(d)
            # 바라보는 방향을 기준으로 전진
            next_r = r + directions[d][0] # 현재방향d에 따라 directions리스트에서 열 변화량 가져옴
            next_c = c + directions[d][1]

            # 왼쪽 방향으로 전진 가능한지 확인
            if 0 <= next_r < N and 0 <= next_c < M and status_list[next_r][next_c] == 0:
                r, c = next_r, next_c
                cleaned = True
                break
        if not cleaned:
            # 네 방향 모두 청소되어 있거나 벽인 경우, 후진 시도
            back_r = r-directions[d][0]
            back_c = c-directions[d][1]

            if 0 <= back_r < N and 0 <= back_c < M and status_list[back_r][back_c] != 1:
                r, c = back_r, back_c
            else:
                # 후진할 수 없으면 종료
                break

    return cleaned_count
def turn_left(direction):
    # 반시계 회전
    if direction == 0:
        turn_direction = direction + 3
        return turn_direction
    else:
        turn_direction = direction - 1
        return turn_direction



N, M  = map(int, input().split())
r, c, d = map(int, input().split())
status_list = []
cleaned_count = 0
for _ in range(N):
    status = list(map(int, input().split()))
    status_list.append(status)

result = robot_clean(N,M,r,c,d,status_list,cleaned_count)
print(result)