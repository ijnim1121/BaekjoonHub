N = int(input())

seat = list(map(int, input().split()))

def refuse(seat):
    reserved_seats = set() #set은 중복된 값을 허용하지 않으므로 같은 좌석 번호가 여러번 추가되는 것을 막을 수 있음
    count = 0
    # for i in range(N-1):
    #     if seat[i] == seat[i+1]:
    #         count += 1
    for s in seat:
        if s in reserved_seats:
            count += 1  # 중복 예약이 발생한 경우
        else:
            reserved_seats.add(s) #예약된 좌석에 추가

    return count
print(refuse(seat))