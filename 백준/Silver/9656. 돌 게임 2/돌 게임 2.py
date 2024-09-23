N = int(input())  # 돌의 개수를 입력받음

# 돌의 개수가 짝수면 창영이가 이기고 홀수면 상근이가 이긴다
if N % 2 == 0:
    print("SK")
else:
    print("CY")