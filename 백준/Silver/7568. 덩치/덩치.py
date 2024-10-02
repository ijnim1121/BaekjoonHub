def body_rank(N, people):
    for i in range(N):
        for j in range(N):
            if i != j:
                if people[i][0]<people[j][0] and people[i][1]<people[j][1]:
                    ranks[i]+=1
    print(*ranks)


# 전체 사람의 수
N = int(input())
# 사람들의 몸무게,키 정보를 담을 리스트
people = []
# 각 사람의 몸무게와 키를 나타내는 양의 정수
for _ in range(N):
    x,y = map(int,input().split())
    people.append((x,y))

# 각 사람의 덩치 등수를 담을 리스트
ranks = [1] * N

body_rank(N, people)