A=int(input())
B=int(input())
C=int(input())
ABC=A*B*C
ABC_str=str(ABC)
for i in range(0,10):
    print(ABC_str.count(str(i)))