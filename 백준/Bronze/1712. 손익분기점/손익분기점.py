A, B, C = map(int, input().split())

# BREAK-EVEN-POINT 손익분기점
# sell-nfix: 제품 한 대를 팔았을 때 얻는 이익
# fix로 나눈다는 것 : 고정비용을 커버하기 위해 몇대를 팔아야하는지
def BEP(fix, nfix, sell):
    if (sell-nfix)>0:
        bep = fix/(sell-nfix)
        if bep > 0:
            return bep + 1 #커버되는 수보다 하나 더 팔아야 이득이 남음
        else:
            return -1
    else:
        return -1
print(int(BEP(A, B, C)))



