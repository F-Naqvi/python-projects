import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"] # list for options that the computer can pick

for i in range(5): # limits the game to 5 rounds
    user_input = input("Please choose Rock, Paper, Scissors, or type Q to quit: ").lower()

    if user_input == "q":
        break #ends the loop

    if user_input not in options: # checks if input is not in list 
        continue

    random_number = random.randint(0, 2)

    computer_pick = options[random_number] # assigns random number to option from list
    print("Computer picked", computer_pick + ".")

    if computer_pick == user_input:
        print("You and the computer have tied. Please try again.")

    elif user_input == "rock" and computer_pick == "scissors":
        user_wins += 1
        print("Congratulations! You have won this round!")
        print("Your score:", user_wins)
        print("Computer score", computer_wins)

    elif user_input == "rock" and computer_pick == "paper":
        computer_wins += 1
        print("Sorry! The computer has won this round!")
        print("Your score:", user_wins)
        print("Computer score", computer_wins)

    elif user_input == "paper" and computer_pick == "scissors":
        computer_wins += 1
        print("Sorry! The computer has won this round!")
        print("Your score:", user_wins)
        print("Computer score", computer_wins)

    elif user_input == "paper" and computer_pick == "rock":
        user_wins += 1
        print("Congratulations! You have won this round!")
        print("Your score:", user_wins)
        print("Computer score", computer_wins)

    elif user_input == "scissors" and computer_pick == "paper":
        user_wins += 1
        print("Congratulations! You have won this round!")
        print("Your score:", user_wins)
        print("Computer score", computer_wins)

    elif user_input == "scissors" and computer_pick == "rock":
        computer_wins += 1
        print("Sorry! The computer has won this round!")
        print("Your score:", user_wins)
        print("Computer score", computer_wins)

if user_wins > computer_wins:
    print("Well done! You have won the game!")

elif user_wins < computer_wins:
    print("The computer has wom the game! Better luck next time!")

else:
    print("The game has ended in a tie!")

print("The final score is " + str(user_wins) + " : " + str(computer_wins))
print("Goodbye!")


# created simple rock-paper-scissors game by asking user to pick options and using random module to generate number and assign to list to represent computer options

# initially created with while-loop to replicate multiple rounds

# added counter and printed score after each round

# added quit option which breaks loop and moves to end sequence

# changed to for-loop to limit the number of rounds to 'x'
