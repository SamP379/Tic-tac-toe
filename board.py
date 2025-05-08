
class Board:

    def __init__(self):
        self.board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    

    def display(self):
        for row in self.board:
            display_row = ""
            for position in row:
                display_row += "|" + position
            display_row += "|"
            print(display_row)
        
    
    def add_move(self, player : str, position : tuple):
        row = position[0]
        column = position[1]
        self.board[row][column] = player
    

    def check_move(self, position : tuple) -> bool:
        row = position[0]
        column = position[1]
        if self.board[row][column] != " ":
            return False
        return True
    

    def check_winner(self, player : str) -> bool:
        success_row = player * 3
        for row in self.board:
            joined_row = "".join(row)
            if joined_row == success_row:
                return True
        for position in range(len(self.board)):
            column = ""
            for row in self.board:
                column += row[position]
            if column == success_row:
                return True
        primary_diagonal = self.board[0][0] + self.board[1][1] + self.board[2][2]
        secondary_diagonal = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if (primary_diagonal == success_row) or (secondary_diagonal == success_row):
            return True
        return False