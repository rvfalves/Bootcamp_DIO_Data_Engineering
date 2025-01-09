# Bootcamp_DIO_Data_Engineering
 Project repository of Bootcamp DIO/NTTDATA - Data Engineering with Python and Power BI

 ## Project version 1 - Description:
Objective: Create a banking system with the following operations: withdraw, deposit and view statement. We were hired by a large bank to develop its new system. This bank wants to modernize its operations and for this purpose it chose the Python language. For the first version of the system we must implement only 3 operations: deposit, withdrawal and statement. It must be possible to deposit positive amounts to the bank account. The v1 of the project works with only 1 user, so we do not need to worry about identifying the branch number and bank account. All deposits must be stored in a variable and displayed in the statement operation. The system must allow 3 daily withdrawals with a maximum limit of R$500.00 per withdrawal. If the user does not have a balance in the account, the system must display a message informing that it will not be able to withdraw the money due to lack of balance. All withdrawals must be stored in a variable and displayed in the statement operation. This operation must list all deposits and withdrawals made in the account. At the end of the list the current account balance must be displayed. If the statement is blank, display the message: No transactions were made. The amounts must be displayed using the format R$ xxx.xx, for example: 1500.45 = R$ 1500.45

## Project version 2 - Description:
Objective: Separate the existing withdrawal, deposit and statement operations into functions. Create two new functions: register user (bank customer) and register bank account (link to the user).
Rules to follow for the functions:
Withdrawal: The withdrawal function must receive arguments only by name (keyword only). Suggested arguments: balance, amount, statement, limit, withdrawal_number, withdrawal_limit. Suggested return: balance and statement.
Deposit: The deposit function must receive arguments only by position (positional only). Suggested arguments: balance, amount, statement. Suggested return: balance and statement.
Statement: The statement function must receive arguments by position and name (positional only and keyword only). Positional arguments: balance, named arguments: statement.
Create user (customer): The program must store the users in a list, a user is composed of: name, date of birth, CPF (Brazilian tax identification number) and address. The address is a string with the format: street, number - neighborhood - city/state abbreviation. Only CPF numbers should be stored. We cannot register two users with the same CPF.
Creating a checking account: The program must store accounts in a list. An account is made up of: branch, account number, user. The account number is sequential, starting at 1. The branch number is fixed: "0001". A user can have more than 1 account, but each account belongs to only 1 user.

## Project version 3 - Description:
Objective: Start modeling the banking system in OOP. Add classes for customers and banking operations: deposit and withdrawal.
Update the implementation of the banking system to store customer and bank account data in objects instead of dictionaries. The code should follow the UML class model below:

![model]([https://file%2B.vscode-resource.vscode-cdn.net/Users/rvf_alves/Documents/Comp/Bootcamp_Python/Projetos/Bootcamp_DIO_Data_Engineering/Trilha%20Python%20-%20desafio.png?version%3D1727097509055])

[https://github.com/rvfalves/Bootcamp_DIO_Data_Engineering/blob/main/Trilha%20Python%20-%20desafio.png]

After completing the modeling of the classes and the creation of the methods, update the methods that handle the menu options to work with the modeled classes.

## Project version 4 - Description:
With the new knowledge acquired about decorators, generators and iterators, you were tasked with implementing the following functionalities in the system:
1. Log decorator: Implement a decorator that is applied to all transaction functions (deposit, withdrawal, account creation, etc.). This decorator should record (print) the date and time of each transaction, as well as the transaction type.
2. Report generator: Create a generator that allows you to iterate over the transactions of an account and return, one by one, the transactions that were performed. This generator should also have a way to filter the transactions based on their type (for example, only withdrawals or only deposits).
3. Custom iterator: Implement a custom iterator AccountIterator that allows you to iterate over all the bank accounts, returning basic information about each account (number, current balance, etc.).

## Project 5 - Description:
In our financial application, we identified the need to track and audit user actions to ensure the security and integrity of operations. The console has been useful so far, but the increasing amount of activity makes it difficult to track all operations in real time. Therefore, we decided that it is vital to log this information to a file for later analysis and ongoing backup.
Modify the current log decorator, which prints information to the console, so that it saves this information to a log file, allowing for easier review and more detailed analysis of user operations.
The decorator should log the following for each function call:
Current date and time
Function name
Function arguments
Value returned by the function
The log file should be called log.txt.
If the log.txt file already exists, the new logs should be appended to the end of the file.
Each log entry should be on a new line.
As an additional added value, it was proposed to create a csv data file to persist user information (name, CPF, date of birth, address) and bank account information (account number and balance from up to 2 accounts per user) between program calls.
