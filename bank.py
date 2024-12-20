current_balance=10000
print("Welcome to the ATM!")
username=(input("Enter your username(Demo user:abc) :"))
if(username != "abc"):
    print("Invalid username, try using the demo account 'abc'")
else:
    password=(input("Enter your password(Demo password:123) :"))
    if(password != "123"):
        print("Invalid password, try using the demo password '123'")
    else:
        print("1. Balance Inquiry")
        print("2. Wihdraw Cash")
        print("3. Deposit Cash")
        print("4. Exit")
        choice=int(input("Please enter your choice (1-4) : "))
        if choice ==1:
             print(f"Your current balance is {current_balance}")
        elif choice ==2:
            amount=int(input("Enter the amount to withdraw: "))
            if amount > current_balance:
                    print("Insufficient balance.")
            else:
                    current_balance -= amount
                    print(f"Withdrawn amount: {amount}")
                    print(f"Remaining balance: {current_balance}")
        elif choice ==3:
             amount=int(input("Enter the amount to deposit: "))
             if amount<=0:
                print("Invalid amount.")
             else:
                    current_balance += amount
                    print(f"Deposited amount: {amount}")
                    print(f"New balance: {current_balance}")
        elif choice==4:
                amount=int(input("Thank you for using out services!!"))
        else:
                print("Invalid choice. Please try again.")


        