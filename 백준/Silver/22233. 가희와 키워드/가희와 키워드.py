import sys
input = sys.stdin.readline

# 키워드의 수와 메모할 글의 수
n, m = map(int, input().split())

# 키워드 입력 받아 집합에 저장
keywords = set(input().strip() for _ in range(n))

# 메모 내용 입력 받아 키워드 제거 작업 수행
for _ in range(m):
    note = input().strip().split(',')
    for word in note:
        if word in keywords:
            keywords.remove(word)
    # 남아 있는 키워드의 개수 출력
    print(len(keywords))
