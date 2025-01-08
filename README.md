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
![model]([https://file%2B.vscode-resource.vscode-cdn.net/Users/rvf_alves/Documents/Comp/Bootcamp_Python/Projetos/Bootcamp_DIO_Data_Engineering/Trilha%20Python%20-%20desafio.png?version%3D1727097509055])([https://github.com/rvfalves/Bootcamp_DIO_Data_Engineering/blob/main/Trilha%20Python%20-%20desafio.png])
After completing the modeling of the classes and the creation of the methods, update the methods that handle the menu options to work with the modeled classes.

## Project 4 - Description:
Com os novos conhecimentos adquiridos sobre decoradores, geradores e iteradores, você foi encarregado de implementar as seguintes funcionalidades no sistema:
1. Decorador de log: Implemente um decorador que seja aplicado a todas as funções de transações (depósito, saque, criação de conta, etc). Esse decorador deve registrar (printar) a data e hora de cada transação, bem como o tipo de transação.
2. Gerador de relatórios: Crie um gerador que permita iterar sobre as transações de uma conta e retorne, uma a uma, as transações que foram realizadas. Esse gerador deve também ter uma forma de filtrar as transações baseado em seu tipo (por exemplo, apenas saques ou apenas depósitos). 
3. Iterador personalizado: Implemente um iterador personalizado ContaIterador que permita iterar sobre todas as contas do banco, retornando informações básicas de cada conta (número, saldo atual, etc).

## Project 5 - Description:
Em nossa aplicação financeira, identificamos a necessidade de rastrear e auditar as ações dos usuários para garantir a segurança e a integridade das operações. O console tem sido útil até agora, mas a quantidade crescente de atividades torna difícil acompanhar todas as operações em tempo real. Portanto, decidimos que é vital registrar essas informações em um arquivo para análise posterior e backup contínuo.
Modificar o atual decorador de log, que imprime informações no console, para que ele salve essas informações em um arquivo de log, possibilitando uma revisão mais fácil e uma análise mais detalhada das operações dos usuários.
O decorador deve registrar o seguinte para cada chamada de função:
Data e hora atuais
Nome da função
Argumentos da função
Valor retornado pela função
O arquivo de log deve ser chamado log.txt.
Se o arquivo log.txt já existir, os novos logs devem ser adicionados ao final do arquivo.
Cada entrada de log deve estar em uma nova linha.

Como uma mais-valia adicional, foi proposta a criação de um arquivo de dados do tipo csv para persistir informações de usuários (nome, cpf, data_nascimento, endereço) e conta bancária (dados de até as 2 primeiras contas por usuários, sendo guardados número-conta e saldo) entre as chamadas do programa. 
