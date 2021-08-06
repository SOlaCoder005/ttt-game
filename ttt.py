# Tic-Tac-Toe Game

"""
Imported Libraries and Modules 
"""
import emoji # Credit: Unicode
import time # Credit: Guru99
import pprint


"""
CONST variables
"""
X = "\U0001F4AA" # human arm symbol 
O = "\U0001F9BE" # mechanical arm symbol
PlayerWon = ""
PlayerLost = ""
PlayerTie = ""
BOARD_SQUARES = 9


def welcome():
    """
    Greets user when they initially run the game.
    """
    print("\nWELCOME TO TIC-TAC-TOE! \U0001F609\n")
    print("This is a place to engage in digital strategic sparing!\n")
    print("Can you put AI in it's place to show it who's boss?\n")
    time.sleep(2.5)
    print("I hope so...\n")
    time.sleep(3)


def r_u_ready_to_play():
    """
    Asks user if they are ready to play.
    """
    yes = "y"
    no = "n"
    
    while True: 
        
        try: 
            answer = input("\nAre you ready to play (y/n)?:\n")

            if answer == yes:
                print("\nOkay! Here's how to play... \U0001F60E\n")
                return game_guides()
                time.sleep(1.5)

            elif answer == no: 
                print("\n\U0001F92F What! Why not?\n")
                print("\n\U0001F612 Okay, maybe next time.\n")
                time.sleep(1)
                return exit()

            else: 
                raise ValueError()

        except ValueError:
            print(
                f"\nSorry, didn't recognise yourt respnse '{answer}'. Try again..."
            )
        #OUTSTANDING ACTION(s)- Create statementent that times out/ allows only 3 incorrect repsonses 

def game_guides():
    """
    Tells user how to play the game
    """
    print(
    
        """
        \U0001F4DC How it works
        -----------------------
        """
    )
    print(
        """ 
        Your battle-ground is formed of 9 squares and looks like this: 

                            0  |  1  |  2
                            --------------
                            3  |  4  |  5
                            --------------
                            6  |  7  |  8

      
        \U0001F449  You can play either as X or O.\n
        \U0001F449  You must align three Xs (or Os).\n
        \U0001F449  They can be aligned horizontally, verticaly or diagonally.\n
        \U0001F449  Do this before the computer and you win the game!\n
        \U0001F449  If both of you run out of moves it you shall daraw a tie!\n
        """
    )
    time.sleep(1.5)

def pick_pieces(): 

    """
    Tells player how to select the piece that they want to use on the game board.
    """

    print("Wait! Before we start, you need to pick a game board piece.\n")
    print(
        """
        \U0001F449 Each piece is assigned to a respective letter.
        """
    )
    print(
        """
            For instance: 
            -------------
        
            a = \U0001F9DE 
            b = \U0001F9D1
            c = \U0001F444
            d = \U0001F441
        """
    )
    print(
        # Do not chnage spacing as this aligns eefectivily in the terminal
        """
        Using the chart below, please select your game piece: are the pieces:

        a   |   b   |   c  
        -----------------
        "\U0001F9DE" | "\U0001F9D1" | "\U0001F444"

        d   |   e   |   f  
        -----------------
        "\U0001F63B" | "\U0001F47B" | "\U0001F916"

        g   |   h   |   i  
        -----------------
        "\U0001F47D" | "\U0001F9E0" | "\U0001F4A3"

        """
    )
    # PlayerPieces = {
    #         "a":"\U0001F9DE", #mermaid
    #         "b":"\U0001F9D1", #cook
    #         "c":"\U0001F444", #mouth
    #         "d":"\U0001F441", #eye
    # }
    # PlayerPiecesDisplay = list(PlayerPieces.values())
    # # print(PlayerPiecesDisplay)


    # v = list(d.values())
    # {names[i]:v[i] for i in range(len(names))}





def exit():
    print(input("\nPlease press ENTER on your keyboard to exit:\n"))
    time.sleep(.5) 
    print("Exiting Game mode...\n") 
    time.sleep(1)
    return welcome()

    
def main(): 
    """
    Contains key functions that allows the game to run. 
    """
    welcome()
    r_u_ready_to_play()
    pick_pieces()
    exit()
main()

