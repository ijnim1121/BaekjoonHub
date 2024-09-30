import sys
input = sys.stdin.readline  # input을 sys.stdin.readline으로 변경하여 입력 속도 향상

# 첫 번째 줄의 입력: 칭호의 개수 N과 전투력 수치의 개수 M
N, M = map(int, input().split())

# 두 번째 줄부터 N개의 줄에 칭호와 그에 대응하는 전투력 수치가 주어짐
titles = []
for _ in range(N):
    title, upper_limit_power = input().split()
    upper_limit_power = int(upper_limit_power)
    if titles and titles[-1][1] == upper_limit_power:
        continue
    titles.append((title, upper_limit_power))

# 그 다음 M개의 전투력 값이 주어짐
powers = []
for _ in range(M):
    fighting_power = int(input())
    powers.append(fighting_power)

# 이진 탐색을 위한 함수 bisect_left
def find_title(value):
    # titles의 인덱스 범위 설정
    left, right = 0, len(titles) - 1
    while left <= right:
        mid = (left + right) // 2
        if titles[mid][1] < value:
            left = mid + 1
            # 찾으려는 값보다 기준값이 작으니까 더 큰 값의 범위에서 봐야해서 left를 mid+1로 이동하는거고
        else:
            right = mid - 1
            # 찾으려는 값보다 기준 값이 크니까 더 작은 값의 범위에서 봐야해서 right를 mid-1로 이동
    return titles[left][0]

# 전투력에 맞는 칭호를 출력
for power in powers:
    print(find_title(power))