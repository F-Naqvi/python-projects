import random  # import 'random' module to generate random numbers

top_of_range = input("Type a number: ")

if top_of_range.isdigit():  # .isdigit() checks if input is a number
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print ("Please type a number larger than 0 next time. ")
        quit()
else:
    print("Please type an integer next time." )
    quit()

random_number = random.randint(1, top_of_range)  # .randint(a,b) generates random number between a and b (including b)

guess_counter = 0

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type an integer next time." )
        continue  # continues the while-loop from the start rather than ending it
    

    if user_guess == random_number:
        guess_counter += 1
        if guess_counter == 1:
            print("You got it! It took you ", guess_counter, " guess ")
        else:
            print("You got it! It took you ", guess_counter, " guesses ")
        break  # ends the while-loop
    else:
        if user_guess <= random_number:
            print("Your guess is too low! Try again!")
        else:
            print("Your guess is too high! Try again!")
        guess_counter += 1



# Began with creating a simple random number generator, then added a user input to select the upper bound of the generator, and another input for the user's guess

# Used if-else statements to add responses to each guess, noticed it responding with "guesses" to singular guess, so added another if-else statement determining whether the number of guesses is singular

# Faced eternal loop problem, so added breaks at the right parts to ensure program ends at comnpletion

# Added guess-counter to keep score

# Decided to add hints for user input, informing whether guess was too high or low, using nested if-else statements
