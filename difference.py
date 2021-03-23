test difference

if player = X:
    if terminal(board) 
        return utility(board)

    v = float('-inf')
    global move
    for action in actions(board):
            min_v = min_value(result(board,action)){
                if terminal(board):
                    return utility(board)
                v = float('inf')
                global move
                for action in actions(board):
                    max_v = max_value(result(board,action)){
                        if terminal(board):
                            return utility(board)
                        v = float('-inf')
                        global move
                        for action in actions(board):
                            min_v = min_value(result(board,action))
                            if v < min_v: #
                                move = action
                            v = max(v, min_v) 
                        return v
                    }
                    if v > max_v: #
                        move = action
                    v = min(v, max_v) 
                return v
            }
            if v < min_v: #
                move = action
            v = max(v, min_v) 
        return v
        

if player(board) = x:
    v = float('-inf')
    move = None

    for action in actions(board):
        min_v = min_value(result(board, action)){
            if terminal(board):
                return utility(board)
            
            v = math.inf

            for action in actions(board):
                num = min(num, max_value(result(board, action)))
            return v
        }

        if min_v > v:
            v = min_v
            move = action
    return move