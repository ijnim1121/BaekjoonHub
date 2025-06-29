n_list=[]

for _ in range(9):
    n_list.append(int(input()))
max_value = max(n_list)
print(max_value)

for i in range(0,9):
    if n_list[i] == max_value:
        print(i+1)