def conveyor_belt_simulation(N, K, durability):
    # 초기 변수 설정
    belt_length = 2 * N
    robots = [False] * N  # 로봇 위치를 저장 (로봇이 윗부분에만 위치하므로 N만큼만 필요)
    steps = 0

    while True:
        steps += 1

        # 1. 벨트 회전
        durability = [durability[-1]] + durability[:-1]  # 벨트를 오른쪽으로 한 칸 회전
        robots = [False] + robots[:-1]  # 로봇 위치도 한 칸 회전

        if robots[-1]:  # 내리는 위치에 로봇이 있다면 내리기
            robots[-1] = False

        # 2. 로봇 이동
        for i in range(N - 2, -1, -1):  # 맨 끝에서부터 앞으로 이동
            if robots[i] and not robots[i + 1] and durability[i + 1] > 0:
                robots[i] = False
                robots[i + 1] = True
                durability[i + 1] -= 1

        if robots[-1]:  # 내리는 위치에 로봇이 있다면 내리기
            robots[-1] = False

        # 3. 올리는 위치에 로봇 올리기
        if durability[0] > 0:
            robots[0] = True
            durability[0] -= 1

        # 4. 내구도 0인 칸이 K개 이상이면 종료
        if durability.count(0) >= K:
            break

    return steps


# 입력 받기
N, K = map(int, input().split())
durability = list(map(int, input().split()))

# 시뮬레이션 실행 및 결과 출력
print(conveyor_belt_simulation(N, K, durability))
