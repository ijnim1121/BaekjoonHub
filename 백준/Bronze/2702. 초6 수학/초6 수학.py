import math
def gcd(a,b): #최대공약수
    return math.gcd(a,b)
def lcm(a,b): #최소공배수
    return math.lcm(a,b)

T = int(input())
for _ in range(T):
    a,b = map(int, input().split())
    print(lcm(a, b), gcd(a, b))