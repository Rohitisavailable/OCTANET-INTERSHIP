ATM Simulator in Python

This project is a Python-based ATM simulator that mimics the functionality of a real-world Automated Teller Machine (ATM). The program features user authentication via a PIN system and provides options for checking balance, withdrawing funds, depositing funds, and exiting the session.

Features

Authentication: Users must enter a valid 4-digit PIN to access their account.

Check Balance: View the current balance of the account.

Withdraw Funds: Withdraw a specified amount from the account, with checks for sufficient funds.

Deposit Funds: Deposit a specified amount into the account.

Exit: End the session safely and display a farewell message.

Interactive Output: Includes typing effects and loading animations for a better user experience.

How to Use

Clone or download the repository.

Ensure you have Python 3 installed on your system.

Run the atm.py script in your terminal or Python IDE:

python atm.py

Follow the on-screen instructions:

Insert your card (simulated via a loading effect).

Enter your 4-digit PIN to authenticate.

Choose an option from the menu to perform a transaction.

Exit the program by selecting the appropriate menu option.

Menu Options

Check Balance: Displays the current account balance.

Withdraw Funds:

Enter the amount you wish to withdraw.

The program checks for sufficient funds before completing the transaction.

Deposit Funds:

Enter the amount you wish to deposit.

The balance is updated after the transaction.

Exit:

Ends the session with a thank-you message.

Code Highlights

Typing Animation:

slow_print: Displays text with a typing effect for improved user engagement.

Loading Effect:

loading_effect: Simulates a loading animation to mimic the time taken for card reading or processing.

Error Handling:

Input validation ensures users enter valid numeric values for PINs and transaction amounts.

Exceptions are handled gracefully to prevent crashes.

Example Interaction

Welcome to the ATM!
Please insert your CARD..........
Enter your 4-digit PIN: 1234
Authorization successful! Welcome to your account.

======= ATM Menu =======
1. Check Balance
2. Withdraw Funds
3. Deposit Funds
4. Exit
========================
Please enter your choice: 1
Your current balance is: ₹5000

======= ATM Menu =======
1. Check Balance
2. Withdraw Funds
3. Deposit Funds
4. Exit
========================
Please enter your choice: 2
Please enter the amount to withdraw: 1000
₹1000 has been withdrawn from your account.
Your updated balance is: ₹4000

Prerequisites

Python 3.6 or higher

Installation

Clone the repository:

git clone https://github.com/your-username/atm-simulator.git

Navigate to the project directory:

cd atm-simulator

Run the script:

python atm.py

Customization

Change the default PIN:

Modify the password variable in the script.

Set an initial balance:

Update the balance variable in the script.

Limitations

This simulator does not connect to a real bank account or database.

PINs are stored as plain text in the script (not secure for production use).

Future Enhancements

Add a database to store multiple user accounts and their details.

Implement encryption for PINs and sensitive data.

Add functionality for mini-statements and account history.

License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

Repository

Find the project on GitHub:

ATM Simulator Repository

Thank you for exploring this project! If you have any questions or suggestions, feel free to reach out.

