
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
    

    def check_move(self, move : tuple) -> bool:
        """Checks if a move is valid. Returns True or False"""
        row = move[0]
        column = move[1]
        try:
            if (row < 0 or row > 2) or (column < 0 or column > 2):
                return False
            elif self.board[row][column] != " ":
                return False
            return True
        except TypeError:
            return False