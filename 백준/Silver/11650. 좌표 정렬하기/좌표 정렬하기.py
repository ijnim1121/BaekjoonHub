n = int(input())
coordinate = []
for _ in range(n):
    a,b = map(int, input().split())
    coordinate.append((a,b))
coordinate.sort()
for x,y in coordinate:
    print(x,y)