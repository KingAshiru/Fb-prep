class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [['.' for _ in range(self.n)] for _ in range(self.n)]
        

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.board[row][col] = 'X'
            if self.is_winner(row, col, 'X'):
                return 1
            else:
                return 0
        else:
            self.board[row][col] = 'O'
            if self.is_winner(row, col, 'O'):
                return 2
            else:
                return 0
            
    def is_winner(self, row: int, col: int, target: str) -> bool:
        n = self.n
        
        def check_row():
            # check the particular row
            for i in range(n):
                if self.board[row][i] == '.':
                    return False
                elif self.board[row][i] != target:
                    return False
            return True
        
        def check_col():
            # check the particular col
            for j in range(n):
                if self.board[j][col] == '.':
                    return False
                elif self.board[j][col] != target:
                    return False
            return True
          
        def check_diagonal1():
            # check the left 2 right diagonal
            # this diagonal uses row - col = 0
            for i in range(n):
                for j in range(n):
                    if i - j == 0:
                        if self.board[i][j] == '.':
                            return False
                        elif self.board[i][j] != target:
                            return False
            return True

        def check_diagonal2():
            # check the digonal from right to left
            # this diagonal uses
            for i in range(n):
                for j in range(n):
                    if i + j == n - 1:
                        if self.board[i][j] == '.':
                            return False
                        elif self.board[i][j] != target:
                            return False
            return True
                    
        # if it hits this point then its true
        return check_row() or check_col() or check_diagonal1() or check_diagonal2()
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
