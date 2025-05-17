N = int(input())
A= map(int, input().split())

def count_good(n, a):
    A = sorted(a)        # 이미 정렬되어 있지만, 일반적으론 여기에 포함
    count = 0

    for i in range(n):
        target = A[i]   # “좋다”인지 확인할 기준 값
        l, r = 0, n-1   # 왼쪽·오른쪽 포인터 초기화

        while l < r:
            if l == i:  # l이 i(타겟 인덱스)면 건너뛰고
                l += 1
                continue
            if r == i:  # r이 i면 건너뛰고
                r -= 1
                continue

            s = A[l] + A[r]
            if s == target:
                count += 1
                break     # 이 i에 대해서는 찾았으니 while 종료
            elif s < target:
                l += 1   # 합이 작으니 left를 오른쪽으로
            else:
                r -= 1   # 합이 크니 right를 왼쪽으로

    return count

print(count_good(N,A))