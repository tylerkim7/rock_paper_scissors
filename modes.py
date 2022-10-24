from random import choice

options = ['rock', 'paper', 'scissors']

def best_of_three():
    """A game of rock paper scissors. First to win two of three rounds wins."""
    print("Best of Three\nIn this mode, you compete against the computer to be the first to win two out of three rounds. Good Luck!")
    score = 0
    comp_score = 0
    while True:
        comp_choice = choice(options)
        user_input = input("rock, paper, or scissors? ")
        if user_input.lower().strip() == comp_choice:
            print("Your opponent chose " + comp_choice + ". It's a Tie!")
            print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
        elif user_input.lower().strip() == "rock":
            if comp_choice == "scissors":
                print("Your opponent chose " + comp_choice + ". You Win!")
                score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            elif comp_choice == "paper":
                print("Your opponent chose " + comp_choice + ". You Lose!")
                comp_score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            else:
                break
        elif user_input.lower().strip() == "paper":
            if comp_choice == "rock":
                print("Your opponent chose " + comp_choice + ". You Win!")
                score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            elif comp_choice == "scissors":
                print("Your opponent chose " + comp_choice + ". You Lose!")
                comp_score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            else:
                break
        elif user_input.lower().strip() == "scissors":
            if comp_choice == "paper":
                print("Your opponent chose " + comp_choice + ". You Win!")
                score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            elif comp_choice == "rock":
                print("Your opponent chose " + comp_choice + ". You Lose!")
                comp_score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            else:
                break
        elif user_input.lower().strip() == "quit":
            print("\nYour score: " + str(score))
            print("Your opponent's score: " + str(comp_score))
            break
        else:
            print("\nSorry, there was an error. Please enter one of the suggested words. ")
        if score == 2 or comp_score == 2:
            if score > comp_score:
                print("\nCongratulations! You Win!")
                print("Your score: " + str(score))
                print("Your opponent's score: " + str(comp_score))
            elif score < comp_score:
                print("\nOh No! You Lost!")
                print("Your score: " + str(score))
                print("Your opponent's score: " + str(comp_score))
            print("We hope to see again soon! ")
            break

def best_of_five():
    """A game of rock paper scissors. First to win three of five rounds wins."""
    print("Best of Five\nIn this mode, you compete against the computer to be the first to win three out of five rounds. Good Luck!")
    score = 0
    comp_score = 0
    while True:
        comp_choice = choice(options)
        user_input = input("rock, paper, or scissors? ")
        if user_input.lower().strip() == comp_choice:
            print("Your opponent chose " + comp_choice + ". It's a Tie!")
            print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
        elif user_input.lower().strip() == "rock":
            if comp_choice == "scissors":
                print("Your opponent chose " + comp_choice + ". You Win!")
                score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            elif comp_choice == "paper":
                print("Your opponent chose " + comp_choice + ". You Lose!")
                comp_score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            else:
                break
        elif user_input.lower().strip() == "paper":
            if comp_choice == "rock":
                print("Your opponent chose " + comp_choice + ". You Win!")
                score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            elif comp_choice == "scissors":
                print("Your opponent chose " + comp_choice + ". You Lose!")
                comp_score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            else:
                break
        elif user_input.lower().strip() == "scissors":
            if comp_choice == "paper":
                print("Your opponent chose " + comp_choice + ". You Win!")
                score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            elif comp_choice == "rock":
                print("Your opponent chose " + comp_choice + ". You Lose!")
                comp_score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            else:
                break
        elif user_input.lower().strip() == "quit":
            print("\nYour score: " + str(score))
            print("Your opponent's score: " + str(comp_score))
            break
        else:
            print("\nSorry, there was an error. Please enter one of the suggested words. ")
        if score == 3 or comp_score == 3:
            if score > comp_score:
                print("\nCongratulations! You Win!")
                print("Your score: " + str(score))
                print("Your opponent's score: " + str(comp_score))
            elif score < comp_score:
                print("\nOh No! You Lost!")
                print("Your score: " + str(score))
                print("Your opponent's score: " + str(comp_score))
            print("We hope to see again soon! ")
            break


def best_of_seven():
    """A game of rock paper scissors. First to win four of seven rounds wins."""
    print("Best of Seven\nIn this mode, you compete against the computer to be the first to win four out of seven rounds. Good Luck!")
    score = 0
    comp_score = 0
    while True:
        comp_choice = choice(options)
        user_input = input("rock, paper, or scissors? ")
        if user_input.lower().strip() == comp_choice:
            print("Your opponent chose " + comp_choice + ". It's a Tie!")
            print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
        elif user_input.lower().strip() == "rock":
            if comp_choice == "scissors":
                print("Your opponent chose " + comp_choice + ". You Win!")
                score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            elif comp_choice == "paper":
                print("Your opponent chose " + comp_choice + ". You Lose!")
                comp_score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            else:
                break
        elif user_input.lower().strip() == "paper":
            if comp_choice == "rock":
                print("Your opponent chose " + comp_choice + ". You Win!")
                score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            elif comp_choice == "scissors":
                print("Your opponent chose " + comp_choice + ". You Lose!")
                comp_score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            else:
                break
        elif user_input.lower().strip() == "scissors":
            if comp_choice == "paper":
                print("Your opponent chose " + comp_choice + ". You Win!")
                score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            elif comp_choice == "rock":
                print("Your opponent chose " + comp_choice + ". You Lose!")
                comp_score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            else:
                break
        elif user_input.lower().strip() == "quit":
            print("\nYour score: " + str(score))
            print("Your opponent's score: " + str(comp_score))
            break
        else:
            print("\nSorry, there was an error. Please enter one of the suggested words. ")
        if score == 4 or comp_score == 4:
            if score > comp_score:
                print("\nCongratulations! You Win!")
                print("Your score: " + str(score))
                print("Your opponent's score: " + str(comp_score))
            elif score < comp_score:
                print("\nOh No! You Lost!")
                print("Your score: " + str(score))
                print("Your opponent's score: " + str(comp_score))
            print("We hope to see again soon! ")
            break

def endless():
    """Endless rock, paper, scissors against the computer"""
    print("Endless Mode\nIn this mode, you compete against the computer until you decide to end the game. See how high you can get your score! Good Luck!")
    score = 0
    comp_score = 0
    while True: 
        comp_choice = choice(options)
        user_input = input("rock, paper, or scissors? Type 'end' at any time to end the game. ")
        if user_input.lower().strip() == comp_choice:
            print("\nYour opponent chose " + comp_choice + ". It's a Tie!")
            print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
        elif user_input.lower().strip() == "rock":
            if comp_choice == "scissors":
                print("\nYour opponent chose " + comp_choice + ". You Win!")
                score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            elif comp_choice == "paper":
                print("\nYour opponent chose " + comp_choice + ". You Lose!")
                comp_score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            else:
                break
        elif user_input.lower().strip() == "paper":
            if comp_choice == "rock":
                print("\nYour opponent chose " + comp_choice + ". You Win!")
                score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            elif comp_choice == "scissors":
                print("\nYour opponent chose " + comp_choice + ". You Lose!")
                comp_score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            else:
                break
        elif user_input.lower().strip() == "scissors":
            if comp_choice == "paper":
                print("\nYour opponent chose " + comp_choice + ". You Win!")
                score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            elif comp_choice == "rock":
                print("\nYour opponent chose " + comp_choice + ". You Lose!")
                comp_score += 1
                print("Current score: \nYou: " + str(score) + "\nOpponent: "+ str(comp_score))
            else:
                break
        elif user_input.lower().strip() == "end" or user_input.lower().strip() == "quit":
            print("\nYour score: " + str(score))
            print("Your opponent's score: " + str(comp_score))
            if score > comp_score:
                print("\nYou win this session!")
            elif score < comp_score:
                print("\nYou lose this session!")
            elif score == comp_score:
                print("\nThis session was a tie!")
            print("\nWe hope to see again soon! ")
            break
        else:
            print("\nSorry, there was an error. Please enter one of the suggested words. ")

def two_player():
    """A two player version of rock, paper, scissors in which two players compete to get the highest score against the computer"""
    print("Two Player\nIn this mode, you and a friend will compete against each other to be the first to win three rounds against the computer. You must win by 2. Good Luck!\n")
    p1_score = 0
    p2_score = 0
    while True:
        if int(p1_score) >= 3 and int(p1_score) >= int(p2_score) + 2:
            print("Player ONE Wins! Congratulations!\nFinal Score:\nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: " + str(p2_score))
            break
        if int(p2_score) >= 3 and int(p2_score) >= int(p1_score) + 2:
            print("Player TWO Wins! Congratulations!\nFinal Score:\nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: " + str(p2_score))
            break
        comp_choice = choice(options)
        p1_input = input("Player ONE's turn. Rock, paper, or scissors? ")
        if p1_input.lower().strip() == comp_choice:
            print("\nThe Computer chose " + comp_choice + ". It's a Tie!")
            print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
        elif p1_input.lower().strip() == "rock":
            if comp_choice == "scissors":
                print("\nThe Computer chose " + comp_choice + ". You Win!")
                p1_score += 1
                print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
            elif comp_choice == "paper":
                print("\nThe Computer chose " + comp_choice + ". You Lose!")
                print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
            else:
                break
        elif p1_input.lower().strip() == "paper":
            if comp_choice == "rock":
                print("\nThe Computer chose " + comp_choice + ". You Win!")
                p1_score += 1
                print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
            elif comp_choice == "scissors":
                print("\nThe Computer chose " + comp_choice + ". You Lose!")
                print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
            else:
                break
        elif p1_input.lower().strip() == "scissors":
            if comp_choice == "paper":
                print("\nThe Computer chose " + comp_choice + ". You Win!")
                p1_score += 1
                print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
            elif comp_choice == "rock":
                print("\nThe Computer chose " + comp_choice + ". You Lose!")
                print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
            else:
                break
        elif p1_input.lower().strip() == "quit":
            print("\nPlayer ONE's score: " + str(p1_score))
            print("Player TWO's score: " + str(p2_score))
            break
        comp_choice = choice(options)
        p2_input = input("Player TWO's turn. Rock, paper, or scissors? ")
        if p2_input.lower().strip() == comp_choice:
            print("\nThe Computer chose " + comp_choice + ". It's a Tie!")
            print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
        elif p2_input.lower().strip() == "rock":
            if comp_choice == "scissors":
                print("\nThe Computer chose " + comp_choice + ". You Win!")
                p2_score += 1
                print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
            elif comp_choice == "paper":
                print("\nThe Computer chose " + comp_choice + ". You Lose!")
                print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
            else:
                break
        elif p2_input.lower().strip() == "paper":
            if comp_choice == "rock":
                print("\nThe Computer chose " + comp_choice + ". You Win!")
                p2_score += 1
                print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
            elif comp_choice == "scissors":
                print("\nThe Computer chose " + comp_choice + ". You Lose!")
                print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
            else:
                break
        elif p2_input.lower().strip() == "scissors":
            if comp_choice == "paper":
                print("\nThe Computer chose " + comp_choice + ". You Win!")
                p2_score += 1
                print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
            elif comp_choice == "rock":
                print("\nThe Computer chose " + comp_choice + ". You Lose!")
                print("Current score: \nPlayer ONE: " + str(p1_score) + "\nPlayer TWO: "+ str(p2_score))
            else:
                break
        elif p2_input.lower().strip() == "quit":
            print("\nPlayer ONE's score: " + str(p1_score))
            print("Player TWO's score: " + str(p2_score))
            break