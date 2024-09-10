T = int(input())
def kin(score):
    score.remove(max(score))
    score.remove(min(score))
    if (max(score) - min(score)) >= 4:
        return "KIN"
    else:
        return sum(score)

for _ in range(T):
    score = list(map(int, input().split()))
    print(kin(score))