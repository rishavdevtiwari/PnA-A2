#Question no.2

print("Welcome to Treasure Land")
dir=(input("Now you shall choose a direction (left/right)"))
if(dir=="right"):
    print("Game Over")
elif(dir=="left"):
    wish=(input("Do you wish to swim or wait"))
    if(wish=="swim"):
        print("Game over")
    elif(wish=="wait"):
        color=(input("Select a color(red/blue/yellow) :"))
        if(color=="blue" or color=="red"):
            print("Game Over")
        elif(color=="yellow"):
            print("You Win")
        else:
            print("Invalid Color Entered")
    else:
        print("Please select from swim or wait!!")
else:
    print("Please choose either left or right")
