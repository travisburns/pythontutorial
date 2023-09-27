import sys
import random 
from enum import Enum 

game_count = 0


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3



    print("")
    playerchoice= input("Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]: 
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)


    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("")
    print("You chose " + str(RPS(player)).replace('RRPS.','') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
    print("")

    def decide_winner(player, computer):

        if player == 1 and computer == 3:
            print("🙌🙌🙌 You win!")

        elif player == 2 and computer == 1:
            print("🙌🙌🙌 You win!")
            
        elif player == 3 and computer == 2:
            print("🙌🙌🙌 You win!")
            
        elif player == computer:
            print("😲😲😲 Draw!")

        else: 
            print("🐍 Python wins!")

    global game_count
    game_count += 1

    print("\nGame count: " + str(game_count))

    print("\nPlay again?")

    while True:
        playagain = input("\nY for yes or \nQ to quit \n}")
        if playagain.lower() not in ["y", "q"]:
            continue
        else: 
            break 

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\ncelebrate!!!")
        print("Thank you for playing! \n")
        sys.exit("Bye!! WAVEE!")
        


play_rps()