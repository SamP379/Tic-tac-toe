import os

class Board:
    """The class to represent the 3x3 grid used in the game Tic Tac Toe"""

    def __init__(self):
        self.board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    

    def display(self):
        """Displays the the current state of the board"""
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
        """Checks if a move is valid or not, returns True/False"""
        row = position[0]
        column = position[1]
        if (row < 0 or row > 2) or (column < 0 or column > 2):
            return False
        elif self.board[row][column] != " ":
            return False
        return True
    

    def add_move(self, player : str, position : tuple):
        """Makes a move for a player, adding their symbol at the given position"""
        row = position[0]
        column = position[1]
        self.board[row][column] = player
    

    def player_won(self, player : str) -> bool:
        """Checks if a given player has won, returns True/False"""
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
        """Checks if the board is full, returns True/False"""
        for row in self.board:
            for position in row:
                if position == " ":
                    return False
        return True