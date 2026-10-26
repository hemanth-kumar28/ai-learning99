def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]

    if ' ' not in board:
        return "Draw"

    return None


def minimax(board, is_max):
    result = check_winner(board)

    if result == 'X':
        return 1
    if result == 'O':
        return -1
    if result == "Draw":
        return 0

    if is_max:  # AI (X) maximizes score
        best = float('-inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(board, False))
                board[i] = ' '  # Undo move

        return best

    else:  # Opponent (O) minimizes score
        best = float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(board, True))
                board[i] = ' '  # Undo move

        return best


def ai_move(board):
    best_score = float('-inf')
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    return move


board = ['X', 'O', 'X',
         'O', 'X', ' ',
         ' ', ' ', 'O']

move = ai_move(board)
board[move] = 'X'

for i in range(0, 9, 3):
    print(board[i], board[i+1], board[i+2])