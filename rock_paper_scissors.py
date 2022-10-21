from random import choice

options = ['rock', 'paper', 'scissors']

start = input("Would you like to play a game of rock paper scissors? (yes or no) ")
if start.lower().strip() == "no":
    flag = "False"
    print("Have a nice day!")
elif start.lower().strip() == "yes":
    flag = "True"


score = 0
comp_score = 0
while flag == "True": 
    comp_choice = choice(options)
    user_input = input("rock paper or scissors? Or type 'quit' to quit. ")
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
        print("Your score: " + str(score))
        print("Your opponent's score: " + str(comp_score))
        if score > comp_score:
            print("You win this session!")
        elif score < comp_score:
            print("You lose this session!")
        elif score == comp_score:
            print("This session was a tie!")
        print("We hope to see again soon! ")
        break
    else:
        print("Sorry, there was an error. Please enter one of the suggested words. ")
    question = input("Would you like to play another round? (yes or no) ")
    if question.lower().strip() == 'yes':
        continue
    elif question.lower().strip() == 'no':
        print("Your score: " + str(score))
        print("Your opponent's score: " + str(comp_score))
        if score > comp_score:
            print("You win this session!")
        elif score < comp_score:
            print("You lose this session!")
        elif score == comp_score:
            print("This session was a tie!")
        print("We hope to see again soon! ")
        break
    else:
        print("Sorry, there was an error. Please enter one of the suggested words. ")
 