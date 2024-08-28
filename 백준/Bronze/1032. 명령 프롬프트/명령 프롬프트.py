# 테스트 케이스 수 입력
T = int(input())
# 첫번째 문자열 입력받기
firstString = list(input())
firstString_len = len(firstString)

for i in range(T-1):
    othersString = list(input())
    for j in range(firstString_len):
        if firstString[j] != othersString[j]:
            firstString[j] = '?'
print(''.join(firstString))