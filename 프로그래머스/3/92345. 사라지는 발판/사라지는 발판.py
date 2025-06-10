def solution(board, aloc, bloc):
    row, col = len(board), len(board[0])
    dc, dr = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    # 주어진 위치가 유효한지
    def is_valid_pos(r,c):
        return 0 <= r < row and 0 <= c < col
    # 현재 플레이어의 위치와 이동 가능한지 여부
    def recursive_func(a_pos, b_pos, visited, step):
        r,c = a_pos if step % 2 == 0 else b_pos
        can_move = False
        is_opponent_winner = True
        win_steps, lose_steps = [],[]
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if is_valid_pos(nr, nc) and (nr, nc) not in visited and board[nr][nc]:
                can_move = True
                if a_pos == b_pos:
                    return True, step+1
                win, steps_left = (recursive_func([nr, nc], b_pos, visited | {(r,c)}, step + 1) if step %2 == 0 else recursive_func(a_pos, [nr, nc], visited | {(r,c)}, step + 1))
                
                is_opponent_winner &= win
                (win_steps if win else lose_steps).append(steps_left)
        if not can_move:
            return False, step
        if is_opponent_winner:
            return False, max(win_steps)
        return True, min(lose_steps)
    _, steps = recursive_func(aloc, bloc, set(), 0)
    return steps
    