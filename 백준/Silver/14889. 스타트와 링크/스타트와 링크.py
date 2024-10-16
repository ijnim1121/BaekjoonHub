from itertools import combinations


def calculate_team_ability(team, ability_map):
    ability = 0
    # 팀의 모든 사람들 간의 능력치 합을 계산
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            ability += ability_map[team[i]][team[j]] + ability_map[team[j]][team[i]]
    return ability


def find_min_ability_diff(n, ability_map):
    players = [i for i in range(n)]
    min_diff = float('inf')

    # N명 중 N//2명을 뽑는 모든 조합을 구한다 (한 팀 구성)
    for team1 in combinations(players, n // 2):
        team1 = list(team1)
        # 팀1에 속하지 않는 나머지 사람들로 팀2를 구성
        team2 = list(set(players) - set(team1))

        # 각 팀의 능력치를 계산
        team1_ability = calculate_team_ability(team1, ability_map)
        team2_ability = calculate_team_ability(team2, ability_map)

        # 두 팀 능력치 차이 계산
        diff = abs(team1_ability - team2_ability)
        # 최소 차이 갱신
        min_diff = min(min_diff, diff)

    return min_diff


N = int(input())  # N명의 인원 수 입력
ability_map = []  # 능력치 배열을 저장할 리스트

# 능력치 배열 입력 받기
for _ in range(N):
    ability_map.append(list(map(int, input().split())))

# 결과 출력
print(find_min_ability_diff(N, ability_map))
