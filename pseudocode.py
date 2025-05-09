"""

class Board:

    function init()
        create the board
    
        
    function display()
        clear the screen 
        display the board
    
        
    function valid_move(position)
        extract the row from the position
        extract the column from the position
        try
            cast the row to an integer
            cast the column to an integer
            if the position is already occupied
                raise an exception
        catch any exception
            return false
        return true

        
    function add_move(player, position)
        add the player to the board
    
        
    function player_won(player)

        create a string to represent a winning row

        for every row in the board
            join every position in the row
            if the joined row equals the winning row
                return true    

        for every column in the board
            join every position in the column
            if the joined column equals the winning row
                return true
        
        if the primary or seconday diagonal equals the winning row
            return true
        
        return false
    
        
    function board_full()
        for every row in the board
            for every position in the row
                if the position equals an empty string
                    return false
        return true
 



                
class TicTacToe: 
    
    function init()
        set the game over state to false
        create the game board
        get the user's player choice
        get the computer's player
    
        
    function get_user_player()
        while the user player is not valid
            get the user to enter their player
        return the user's player
    
        
    function get_computer_player()
        if the user choose X 
            return O
        return X


    function get_user_move()
        while the user move is not valid
            get the user to enter a move
        return the user's move
    
        
    function get_computer_move()
        while the computer's move is not valid
            generate a random move
        return the computer's move
    
    
    function game_over()
        if the user has won or the computer has won
            return true
        elif the board is full
            return true
        return false
    
        
    function end_game()
        if the user won
            display a you win message
        else
            display a you lose message
        set the game over state to true


    function main_loop()
        while the game is not over
            display the board
            get the user move 
            add the user move to the board
            if the game is over
                end the game
            else
                get the computer move
                add the computer move to the board
                if the game is over
                    end the game
                    
"""