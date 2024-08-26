X, Y = map(int, input().split())

string_X= str(X)
string_Y= str(Y)

string_reversed_X = string_X[::-1]
string_reversed_Y = string_Y[::-1]

reversed_X = int(string_reversed_X)
reversed_Y = int(string_reversed_Y)

total_sum = reversed_X + reversed_Y

string_sum = str(total_sum)
reverse_sum = string_sum[::-1]

print(int(reverse_sum))


