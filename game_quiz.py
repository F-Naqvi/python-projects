print("Welcome to my computer game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": # .lower converts input to lower case
    quit()

print("Okay! Let's play  :) ")
score = 0
    

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct! ")
    score +=1 # += adds to the counter
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct! ")
    score +=1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct! ")
    score +=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!") # str() converts integer variable to string
