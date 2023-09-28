import sys
import random


 def guess_number(name='PlayerOne'):
     game_count = 0
     player_wins = 0
     
     def play_guess_number():
         nonlocal name
         nonlocal player_wins

         playerchoice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3. \n\n")

            if playerchoice not in ["1", "2", "3"]:
               print(f"{name}, please enter 1, 2, or 3.")
               return play_guess_number()
         computerchoice = random.choice("123")

         print(f"\n{name}, you chose {playerchoice}.")
         print(
            f"I was thinking about the number {computerchoice}. \n"
         )
     
        player = int(playerchoice)

        computer = int(computerchoice)
     
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
               player_wins +=1
               return f"{name}, you win!"
            else:
               return f"Sorry, {name}. Better luck next time."
            
        game_result = decide_winner(player, computer)
     
        print(game_result)