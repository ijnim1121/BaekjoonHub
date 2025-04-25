def solution(s):
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    if stack:
        answer = 0
    else:
        answer = 1
    return answer
            