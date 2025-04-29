def solution(board, moves):
    stack = [[] for _ in range(len(board[0]))]
    
    for i in range(len(board) -1, -1, -1):
        for j in range(len(board)):
            if board[i][j]:
                stack[j].append(board[i][j])
                
    bucket = []
    
    answer = 0
    
    for m in moves:
        if stack[m-1]:
            doll = stack[m-1].pop()
            
            if bucket and bucket[-1] == doll:
                bucket.pop()
                answer += 2
            else:
                bucket.append(doll)
                
    return answer
        
    