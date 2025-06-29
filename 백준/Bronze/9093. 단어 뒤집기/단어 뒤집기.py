T = int(input())
for _ in range(T):
    case = input().split()
    reverse_case=[]
    for i in range(len(case)):
        reverse_case.append(case[i][::-1])
    result=[]
    result=' '.join(reverse_case)
    print(result)