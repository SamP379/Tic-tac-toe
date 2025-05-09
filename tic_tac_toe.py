import random
from board import Board


class TicTacToe:
    """A class to represent the game Tic Tac Toe. The class has a board object attribute, a boolean variable game_over
    attribute, and user and computer attributes to represent which symbols they are each playing as."""

    def __init__(self):
        self.game_over = False
        self.board = Board()
        self.user = self.get_user_player()
        self.computer = self.get_computer_player()
    

    def get_user_player(self):
        "Prompts the user to select a symbol (X or O) and returns their choice"
        while True:
            user_player = input("\nEnter your player (X or O): ").upper()
            if user_player in ("X", "O"):
                break
        return user_player
    

    def get_computer_player(self):
        "Returns the computer's symbol (opposite of what the user choose)"
        if self.user == "X":
            return "O"
        return "X"
    

    def get_user_move(self) -> tuple:
        """Returns the position (row, column) that the user want's to place their symbol (X or O)"""
        while True:
            try:
                row = int(input("\nEnter row: "))
                column = int(input("Enter column: "))
                move = (row, column)
                if not self.board.valid_move(move):
                    raise Exception
                break
            except Exception:
                print("\nEnter a valid move")
        return move
    

    def get_computer_move(self) -> tuple:
        """Generates a random position on the board (row, column) for the computer's move"""
        while True:
            row = random.randint(0,2)
            column = random.randint(0,2)
            move = (row,column)
            if self.board.valid_move(move):
                break
        return move
    

    def check_game_over(self):
        """Checks if the game is over and returns True/False"""
        if self.board.player_won(self.user) or self.board.player_won(self.computer):
            return True
        elif self.board.board_full():
            return True
        return False


    def end_game(self):
        """Displays a game over message and sets the game state to be over"""
        if self.board.player_won(self.user):
            print("\nYou win!")
        else:
            print("\nYou lose!")
        self.game_over = True
    

    def main_loop(self):
        """The main loop of Tic Tac Toe"""
        while not self.game_over:
            self.board.display()
            user_move = self.get_user_move()
            self.board.add_move(self.user, user_move)
            if self.check_game_over():
                self.end_game()
            else:
                computer_move = self.get_computer_move()
                self.board.add_move(self.computer, computer_move)
                if self.check_game_over():
                    self.end_game()