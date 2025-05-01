def solution(want, number, discount):
    dic = {}
    count = 0
        
    for i in range(len(discount) - 9):
        discount_days = discount[i:(i+10)]
        
        dic = dict(zip(want, number))
        
        for day in discount_days:
            if day in dic:
                dic[day] -= 1
                
        if all(value == 0 for value in dic.values()):
            count += 1
    return count