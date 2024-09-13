import sys

def stack_method(command, X=None): #X=None -> 매개변수의 기본 값 설정
    # 스택 초기화 - 전역변수로 선언하여 모든 명령에서 접근할 수 있도록 함
    global stack
    if command == 1:
        stack.append(X)
    elif command == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == 3:
        print(len(stack))
    elif command == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == 5:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)

# 스택 초기화
stack = []

# 첫째 줄에 명령의 수 N을 입력받습니다.
N = int(sys.stdin.readline().strip())

# N개의 명령을 처리합니다.
for _ in range(N):
    command = list(map(int, sys.stdin.readline().strip().split()))

    if command[0] == 1:  # 삽입 명령인 경우
        stack_method(command[0], command[1])
    else:  # 나머지 명령은 하나의 인자만 필요
        stack_method(command[0])