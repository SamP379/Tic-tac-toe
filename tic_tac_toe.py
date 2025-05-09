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
            user_player = input("\nEnter your player (X or O): ").upper()
            if user_player in ("X", "O"):
                break
        return user_player
    

    def get_computer_player(self):
        if self.user == "X":
            return "O"
        return "X"
    

    def get_user_move(self):
        while True:
            row = input("\nEnter row: ")
            column = input("Enter column: ") 
            move = (row, column)
            if self.board.valid_move(move):
                break 
        return move
    

    def get_computer_move(self):
        while True:
            row = random.randint(0,2)
            column = random.randint(0,2)
            move = (row,column)
            if self.board.valid_move(move):
                break
        return move
    

    def game_over(self):
        if self.board.player_won(self.user) or self.board.player_won(self.computer):
            return True
        elif self.board.board_full():
            return True
        return False


    def end_game(self):
        if self.board.player_won(self.user):
            print("\nYou win!")
        else:
            print("\nYou lose!")
        self.game_over = True
    

    def main_loop(self):
        while not self.game_over:
            self.board.display()
            user_move = self.get_user_move()
            self.board.add_move(self.user, user_move)
            if self.game_over():
                self.end_game()
            else:
                computer_move = self.get_computer_move()
                self.board.add_move(self.computer, computer_move)
                if self.game_over():
                    self.end_game()