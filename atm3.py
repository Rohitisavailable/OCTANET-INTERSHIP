import time
import sys

def slow_print(text, delay=0.05):
    """Print text with a typing animation effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

def loading_effect(message, duration=3, interval=0.3):
    """Simulate a loading effect with dots."""
    sys.stdout.write(message)
    sys.stdout.flush()
    for _ in range(int(duration / interval)):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(interval)
    print()  # Move to the next line when done

# Start of the program
slow_print("Welcome to the ATM!", delay=0.07)
time.sleep(1)

loading_effect("Please insert your CARD", duration=4, interval=0.5)  # Card inserting effect
time.sleep(2)

password = 1234
balance = 5000

# Requesting PIN with validation
while True:
    pin_input = input("Enter your 4-digit PIN: ")
    if pin_input.isdigit() and len(pin_input) == 4:  # Validate the PIN input
        pin = int(pin_input)
        break
    else:
        slow_print("Invalid input. Please enter a 4-digit numeric PIN.", delay=0.05)

if pin == password:
    slow_print("Authorization successful! Welcome to your account.\n", delay=0.05)
    time.sleep(1)
    while True:
        print("""
        ======= ATM Menu =======
        1. Check Balance
        2. Withdraw Funds
        3. Deposit Funds
        4. Exit
        ========================
        """)

        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            slow_print("Invalid input. Please select a valid option.", delay=0.05)
            time.sleep(1)
            continue

        if option == 1:
            slow_print(f"Your current balance is: ₹{balance}\n", delay=0.05)
            time.sleep(1)

        elif option == 2:
            try:
                withdraw_amount = int(input("Please enter the amount to withdraw: "))
                if withdraw_amount > balance:
                    slow_print("Insufficient funds! Transaction declined.", delay=0.05)
                else:
                    balance -= withdraw_amount
                    slow_print(f"₹{withdraw_amount} has been withdrawn from your account.", delay=0.05)
                    slow_print(f"Your updated balance is: ₹{balance}\n", delay=0.05)
            except ValueError:
                slow_print("Invalid input. Please enter a valid amount.", delay=0.05)
            time.sleep(1)

        elif option == 3:
            try:
                deposit_amount = int(input("Please enter the amount to deposit: "))
                balance += deposit_amount
                slow_print(f"₹{deposit_amount} has been deposited to your account.", delay=0.05)
                slow_print(f"Your updated balance is: ₹{balance}\n", delay=0.05)
            except ValueError:
                slow_print("Invalid input. Please enter a valid amount.", delay=0.05)
            time.sleep(1)

        elif option == 4:
            slow_print("Thank you for using our service! Have a great day!", delay=0.05)
            time.sleep(2)
            break

        else:
            slow_print("Invalid choice. Please select a valid option from the menu.", delay=0.05)
            time.sleep(1)

else:
    slow_print("Wrong PIN! Please try again.", delay=0.05)
    time.sleep(2)
