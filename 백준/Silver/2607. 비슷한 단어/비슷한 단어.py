n = int(input())
base = list(input())
result = 0

for _ in range(n-1):
    compare = base[:] # 복사본
    words = input()
    count = 0

    for word in words:
        if word in compare:
            compare.remove(word)
        else:
            count += 1

    if count <= 1 and len(compare) <= 1:
        # words에서 추가된 문자가 1개 이하 / base에서 남은 문자가 1개 이하.
        result += 1

print(result)