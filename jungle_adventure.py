# 34.Create a Python program that greets the user with the message "Welcome to
# the Jungle Adventure". Then, ask the user whether they want to go "left" or
# "right". If they choose "right", print "Game Over". If they choose "left", ask if
# they want to "climb a tree" or "explore the cave". If they choose "climb a tree",
# print "Game Over". If they choose "explore the cave", ask them to choose
# between "bear", "tiger", or "snake". If they choose "bear" or "tiger", print
# "Game Over". If they choose "snake", print "You Win".

print("Welcome to the Jungle Adventure")
user_choice=input("Do you want to go left or right : ")
if user_choice.lower()=="right":
    print("Game Over")
elif user_choice.lower()=="left":
    user_choice=input("Do you want to climb a tree or explore the cave : ")
    if user_choice.lower()=="climb a tree":
        print("Game Over")
    elif user_choice.lower()=="explore the cave":
        user_choice=input("choose(bear/tiger/snake)")
        if user_choice.lower()=="bear" or user_choice.lower()=="tiger":
            print("Game Over")
        elif user_choice.lower()=="snake":
            print("You win!")
        else:
            print("Invalid choice!")
    else:
        print("Invalid choice!")
else:
    print("Invalid choice!")