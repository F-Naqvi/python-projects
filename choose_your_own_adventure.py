name = input("please type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    print("")

else:
    print("Invalid answer. You lose.")