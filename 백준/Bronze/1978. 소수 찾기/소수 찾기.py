N=int(input())
n_list=list(map(int, input().split()))
result = 0

for i in range(0, N):
    count = 0
    for j in range(1, n_list[i]):
        if n_list[i] % j == 0:
            count += 1
    if count == 1:
        result += 1
print(result)