
def deposit(balance, value, bank_statement, /):
    if value > 0:
        balance += value
        bank_statement += f"Depósito de R$ {value:.2f}\n"
        print(f"Depósito de R$ {value:.2f} realizado com sucesso.")
    else:
        print("Erro. O valor a ser depositado deve ser um número maior que zero.")
    return balance, bank_statement

def withdraw(*, balance, value, bank_statement, limit, withdraw_number, withdraw_limit):
    if withdraw_number < withdraw_limit:
        if value >0:
            if value <= limit:
                if value <= balance:
                    balance -= value
                    bank_statement += f"Saque de R$ {value:.2f}\n"
                    print(f"Saque de R$ {value:.2f} realizado com sucesso.")
                    withdraw_number += 1
                else:
                    print(f"Lamentamos, mas o valor de saque desejado é maior que o seu saldo de R$ {balance:.2f}.")
            else:
                print(f"Lamentamos, mas você excedeu o limite de R$ {limit:.2f} por saque.")
        else:
            print("Erro. O valor a ser sacado deve ser um número maior que zero.")
    else:
        print("Lamentamos, mas você excedeu o número de saques diários")
    
    return withdraw_number, balance, bank_statement

def statement(balance,/,*, bank_statement):
    print("\nEXTRATO DE CONTA")
    if bank_statement == "":
        print("Não foram realizadas movimentações")
    else:
        print(bank_statement)
        print(f"\nSaldo de conta: R$ {balance:.2f}")

def register_user(cpf, name, birth_date, address, users):
    for user in users:
        if cpf == user["cpf"]:
            print("Este CPF já foi cadastrado. Tente novamente.")
            return users
    users.append({
                "cpf": cpf,
                "name": name,
                "birth_date": birth_date,
                "address": address
            })
    print("Cliente cadastrado com sucesso.")
    return users

def create_account(cpf, users, accounts):
    for user in users:
        if cpf == user["cpf"]:
            accounts.append({
                "agencia": "0001",
                "numero_conta": len(accounts)+1,
                "user": user,
                "balance": 0,
                "bank_statement": "",
                "withdraw_number": 0
            })
            print("Conta cadastrada com sucesso.")
            return accounts
    print("Este CPF não foi cadastrado. Efetue o cadastro de usuário antes de cadastrar sua conta.")
    return accounts

def list_users(users):
    for user in users:
        print("\n CPF: {user[cpf]} \n Nome: {user[name]} \n Data de nascimento: {user[birth_date]} \n Endereço: {user[address]}")

def list_accounts(accounts):
    for account in accounts:
        print("\n Agência: {account[agency]} \n Conta-corrente: {account[account_number]} \n Cliente: {account[user][name]} \n CPF: {account[user][cpf]}")

menu = """

Escolha a operação de deseja executar:
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar conta-corrente
[u] Cadastrar usuário
[lc] Listar contas
[lu] Listar usuários
[q] Sair

=> """

#balance = 0
limit = 500
#bank_statement = ""
#withdraw_number = 0
WITHDRAW_LIMIT = 3
users=[]
accounts=[]

while True:

    option = input(menu)

    if option == "d":
        account_number = int(input("Informe o número da sua conta: "))
        value = float(input("Informe o valor deseja depositar: "))
        balance, bank_statement = deposit(balance, value, bank_statement)

    elif option == "s":
        value = float(input("Informe o valor deseja sacar: "))
        withdraw_number, balance, bank_statement = withdraw(balance=balance, value=value, bank_statement=bank_statement, limit=limit, withdraw_number=withdraw_number, withdraw_limit=WITHDRAW_LIMIT)

    elif option == "e":
        statement(balance, bank_statement=bank_statement)
   
    elif option == "c":
        cpf = input("Informe o seu CPF (apenas números): ")
        accounts = create_account(cpf, users, accounts)

    elif option == "u":
        cpf = input("Informe o seu CPF (apenas números): ")
        name = input("Informe o seu nome: ")
        birth_date = input("Informe sua data de nascimento (formato DD-MM-YYYY): ")
        address = input("Informe o seu endereço (logradouro, numero - bairro - cidade/sigla estado): ")
        users = register_user(cpf, name, birth_date, address, users)
   
    elif option == "lc":
        list_accounts(accounts)

    elif option == "lu":
        list_users(users)
    
    elif option == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
