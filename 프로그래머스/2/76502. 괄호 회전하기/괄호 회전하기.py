def solution(s):
    list_s = list(s)
    answer = 0
    for i in range(len(s)):
        stack = []
        for c in list_s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)
            elif c == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(c)
            elif c == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(c)

        if i != len(s)-1:
            popped_element = list_s.pop(0)
            list_s.append(popped_element)
            
        if not stack:
            answer += 1
        
    return answer