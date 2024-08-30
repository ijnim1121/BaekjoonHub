t = int(input())
shopLocation=[]

for _ in range(t):
    n = int(input())
    locations = list(map(int, input().split()))
    shopLocation.append(locations)  # 개별 리스트를 추가
    # 헷갈렸던 부분 !!
    # 처음에 리스트를 locations += list(map(int, input().split()))
    # 이렇게 받아서 두 리스트가 한 리스트로 합쳐져서 출력이되어, 개별 리스트 추가하는 방법으로 [ [],[] ] 이런형식으로 바꿈

def minWalkDistance(locations):
    sortedLocation = sorted(locations)
    close = sortedLocation[0]
    distant = sortedLocation[-1]
    minwalkdistance = (distant-close)*2
    return minwalkdistance

for locations in shopLocation:
    print(minWalkDistance(locations))

    # [ [],[] ]리스트가 이런 형식으로 들어오다보니, 처음엔 함수 내에서 반복문을 작성하다가 해결이 안되서
    # 이부분은 검색을 해서 이런식으로 해결할 수 있었다.
