# 33. Create a Python program that greets the user with the message "Welcome to
# the Haunted House". Then, ask the user whether they want to go "upstairs" or
# "downstairs". If they choose "downstairs", print "Game Over". If they choose
# "upstairs", ask if they want to "enter the room" or "stay outside". If they choose
# "enter the room", print "Game Over". If they choose "stay outside", ask them
# to choose between "ghost", "vampire", or "werewolf". If they choose "ghost" or
# "vampire", print "Game Over". If they choose "werewolf", print "You Win".

print("Welcome to the Haunted House")
user_choice = input("Do you want to go upstairs or downstairs? ")
if user_choice.lower() == "downstairs":
    print("Game Over")
elif user_choice.lower() == "upstairs":
    user_choice = input("Do you want to enter the room or stay outside? ")
    if user_choice.lower() == "enter the room":
        print("Game Over")
    elif user_choice.lower() == "stay outside":
        user_choice=input("Choose (ghost/vampire/werewolf) : ")
        if user_choice.lower() in ["ghost","vampire"]:
            print("Game Over")
        elif user_choice.lower() == "werewolf":
            print("You Win!!!")
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")
    