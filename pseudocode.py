"""


class Board:

    function init()
        pass
    
        
    function add_move(player, position)
        add the player to the board
    
        
    function check_winner(player)
    
        create compare string variable

        for every row in the board
            join every position in the row into a string
            if the joined string equals the compare string
                return true    

        for every column in the board
            join every position in the column into a string
            if the joined string equals the compare string
                return true
        
        if the primary or seconday diagonal equals the compare string
            return true
        
        return false
        



                
class TicTacToe: 
    
    function init()
        set the game is over to be false
        create the game board
        get the user's player choice
        set the computer's player


    function get_user_move()
        get the user to enter a move
        while the move is not valid
            get the user to enter a move
        return the user move
    
        
    function get_computer_move()
        generate a random position on the board
        while the move is not valid
            generate a random position on the board
        return the random position


    function main_loop()
        while the game is not over
            display the board
            get the user move 
            add the user move to the board
            if the user has won
                display a you win message
                break out of the while loop
            get the computer's move
            add the computer's move to the board
            check if the computer has won
                display a you lose message
                break out of the while loop


"""