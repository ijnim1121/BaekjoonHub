def max_hamburgers_eaten(n, k, table):
    people = []
    burgers = []

    for i in range(n):
        if table[i] == 'P':
            people.append(i) # 위치를 저장
        elif table[i] == 'H':
            burgers.append(i)

    eaten = 0
    i, j = 0, 0

    # 투 포인터로 최적 햄버거 먹기
    while i < len(people) and j < len(burgers):
        if abs(people[i] - burgers[j]) <= k:
            # 사람이 햄버거를 먹을 수 있는 경우
            eaten += 1
            i += 1
            j += 1
        elif people[i] < burgers[j]:
            # 사람이 햄버거에 도달할 수 없는 경우 사람 포인터 증가
            i += 1
        else:
            # 햄버거가 사람에게 도달할 수 없는 경우 햄버거 포인터 증가
            j += 1

    return eaten

n, k = map(int, input().split())
table = input().strip()

print(max_hamburgers_eaten(n, k, table))