n = int(input())
for _ in range(n):
    case=list(input())
    count=0
    sum=0
    for s in case:
        if s == 'O':
            count += 1
            sum += count
        else:
            count =0
    print(sum)
        