def nqueens(n):
    board = [-1]*n

    def is_safe(row,col):
        for r in range(row):
            c = board[r]
            if(col == board[r]):
                return False
            
            if(abs(r-row) == abs(c-col)): #comparing with previously placed queen ,not current one
                return False

        return True

    def solve(row):
        if(row==n):
            print("solution found")
            for i in range(row):
                print("." * board[i] + "Q" + "." * (n - board[i] - 1))
            return True
        
        for col in range(n):
            if is_safe(row,col):
                board[row] = col   #updaing col value if SAFE.

                if solve(row+1):  #check row+1 INSIDE if-block
                    return True
            
                board[row] = -1 #backtrack

        return False

    if not solve(0):
        print('no solutions exists')

nqueens(4)
