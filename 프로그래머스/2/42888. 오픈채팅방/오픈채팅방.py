def solution(record):
    user_dict = {}
    answer = []
    for r in record:
        part = r.split()
        if part[0] == "Enter" or part[0] == "Change":
            uid = part[1]
            nickname = part[2]
            user_dict[uid] = nickname
        
    for r in record:
        part = r.split()
        if part[0] == "Enter":
            if part[1] in user_dict:
                answer.append(user_dict[part[1]] + "님이 들어왔습니다.")
        if part[0] == "Leave":
            if part[1] in user_dict:
                answer.append(user_dict[part[1]] + "님이 나갔습니다.")
    
    return answer