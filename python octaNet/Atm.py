balance = 1000
pin = 1234
transaction_history = []
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Cash")
    print("4. Change PIN")
    print("5. Transaction History")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")
    if choice == '1':
        print(f"Current balance: ${balance}")
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance = balance-amount
            transaction_history.append(f"Withdrew ${amount}")
            print(f"Withdraw Cash:${amount}")
    elif choice == '3':
        amount = float(input("Enter amount to deposit: "))
        balance = balance+amount
        transaction_history.append(f"Deposited ${amount}")
        print(f"Deposited: ${amount}")
    elif choice == '4':
        new_pin = int(input("Enter new PIN: "))
        pin = new_pin
        transaction_history.append("PIN changed")
        print("PIN changed successfully.")
    elif choice == '5':
        if not transaction_history:
            print("No transactions yet.")
        else:
            for transaction in transaction_history:
                print(transaction)
    elif choice == '6':
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid option. Please try again.")
