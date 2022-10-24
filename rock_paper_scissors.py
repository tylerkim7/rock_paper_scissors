from random import choice
import modes

options = ['rock', 'paper', 'scissors']





start = input("Would you like to play a game of rock paper scissors? (yes or no) ")
while True:
    if start.lower().strip() == "no":
        break
    if start.lower().strip() == "yes":
        mode = input("\nWhat gamemode would you like to play? (1-5) Type 'quit' at any time to quit. \n1. Best of Three\n2. Best of five\n3. Best of seven\n4. Endless\n5. Two Player\n")
        if str(mode).lower().strip() == "1":
            modes.best_of_three()
        if str(mode).lower().strip() == "2":
            modes.best_of_five()
        if str(mode).lower().strip() == "3":
            modes.best_of_seven()
        if str(mode).lower().strip() == "4":
            modes.endless()
        if str(mode).lower().strip() == "5":
            modes.two_player()
        if str(mode).lower().strip() == "quit":
            break
    replay = input("\n\nWould you like to play again? (yes/no) ")
    if replay.lower().strip() == "no":
        break
    if replay.lower().strip() == "yes":
        continue
