import random
from board import Board


class TicTacToe:

    def __init__(self):
        self.game_over = False
        self.board = Board()
        self.user = self.get_user_player()
        self.computer = self.get_computer_player()
    

    def get_user_player(self):
        while True:
            user_player = input("Enter your player (X or O): ").upper()
            if user_player in ("X", "O"):
                break
        return user_player
    

    def get_computer_player(self):
        if self.user_player == "X":
            return "O"
        return "X"
    

    def get_user_move(self):
        while True:
            try:
                row = int(input("Enter row: "))
                column = int(input("Enter column: "))
                move = (row, column)
                if (row < 0 or row > 2) or (column < 0 or column > 2) or (not self.board.check_move(move)):
                    raise Exception
                break
            except Exception:
                print("Enter a valid move.")
        return move
    

    def get_computer_move(self):
        while True:
            row = random.randint(0,2)
            column = random.randint(0,2)
            move = (row,column)
            if self.board.check_move(move):
                break
        return move
    

    def end_game(self, user_won : bool):
        if user_won:
            print("You win!")
        else:
            print("You lose!")
        self.game_over = True
    

    def main_loop(self):
        while not self.game_over:
            self.board.display()
            user_move = self.get_user_move()
            self.board.add_move(user_move)
            if self.board.check_winner(self.user):
                self.end_game(True)
            else:
                computer_move = self.get_computer_move()
                self.board.add_move(computer_move)
                if self.board.check_winner(self.computer):
                    self.end_game(False)