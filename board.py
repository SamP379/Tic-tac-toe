import os

class Board:

    def __init__(self):
        self.board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    

    def display(self):
        os.system("cls")
        print("")
        for row in self.board:
            display_row = ""
            for position in row:
                display_row += "|" + position
            display_row += "|"
            print(display_row)
        print("")
    

    def valid_move(self, position : tuple):
        row = position[0]
        column = position[1]
        try:
            row = int(row)
            column = int(column)
            if (row < 0 or row > 2) or (column < 0 or column > 2):
                raise Exception
            elif self.board[row][column] != " ":
                raise Exception
        except Exception:
            return False
        return True
    

    def add_move(self, player : str, position : tuple):
        row = position[0]
        column = position[1]
        self.board[row][column] = player
    

    def player_won(self, player : str) -> bool:
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
    

    def board_full(self) -> bool:
        for row in self.board:
            for position in row:
                if position == " ":
                    return False
        return True