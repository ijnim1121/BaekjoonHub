T = int(input())
for _ in range(T):
    case = input()
    stack = []
    flag = True 

    for char in case:
        if char == '(':
            stack.append(char)
        else:
            if not stack: 
                flag = False
                break
            stack.pop()

    if flag and len(stack) == 0:
        print('YES')
    else:
        print('NO')