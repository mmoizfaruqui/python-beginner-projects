# ------------------------------------------
# Mini Bank Management System
# Main program
# Imports functions from Bankingfunctions.py
# ------------------------------------------

import Bankingfunctions

# Starting account balance
Balance = 500000

# Lists to store transaction history
Withdrew = []
Deposits = []

# User must type "Start" to begin the program
choice = input("Press Start to initiate:")

# Keep displaying the menu until the user exits
while choice == "Start":

    # Main menu
    print(
        "Press "
        "1:To Deposit "
        "2:Withdrew "
        "3:Check Balance availaible "
        "4:Check Transaction History "
        "5:Type 5 to finish"
    )

    Option = int(input("Enter the number:"))

    # -------------------------------
    # Deposit Money
    # -------------------------------
    if Option == 1:

        # Call deposit() function
        a = Bankingfunctions.deposit()

        # Do not allow negative deposits
        while a < 0:
            print("Please enter a positive amount")
            a = Bankingfunctions.deposit()

        # Add deposited amount to balance
        Balance = Balance + a

        print("You just depsoited:", a)

        # Save transaction in history
        Deposits.append(a)

    # -------------------------------
    # Withdraw Money
    # -------------------------------
    elif Option == 2:

        # Call withdrawal function
        b = Bankingfunctions.withdrawl()

        # Keep asking until positive amount is entered
        while b < 0:
            print("Please enter a positive amount")
            b = Bankingfunctions.withdrawl()

        # Check if enough balance is available
        if Balance >= b:

            # Update balance
            Balance = Balance - b

            # Store withdrawal in history
            Withdrew.append(b)

            print("you just withdrew", b)

        else:
            print("your balance is not sufficient for the withdrawl")

    # -------------------------------
    # Check Current Balance
    # -------------------------------
    elif Option == 3:

        print("Your current balance is", Balance)

    # -------------------------------
    # Transaction History
    # -------------------------------
    elif Option == 4:

        print(
            "You want history of deposits, withdrawls or both "
            "press D to check deposits, W for withdrawls , B for both"
        )

        ask = input("Enter:")

        # Deposit history
        if ask == "D":
            print("this si the list of your Deposits history", Deposits)

        # Withdrawal history
        elif ask == "W":
            print("this si the list of your Withdrawls history", Withdrew)

        # Both histories
        elif ask == "B":
            print("this is the list of your Deposits history", Deposits)
            print("this is the list of your Withdrawsl history", Withdrew)

    # -------------------------------
    # Exit Program
    # -------------------------------
    elif Option == 5:
        break

    # Runs if user enters an invalid menu option
    else:
        print("Invalid Option")