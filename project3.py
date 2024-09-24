
from abc import ABC, abstractmethod

def deposit(account, value, /):
    if value > 0:
        account["balance"] += value
        account["bank_statement"] += f"Depósito de R$ {value:.2f}\n"
        print(f"Depósito de R$ {value:.2f} realizado com sucesso à conta {account["account_number"]}")
    else:
        print("Erro. O valor a ser depositado deve ser um número maior que zero.")
    return account

def withdraw(*, account, value, limit, withdraw_limit):
    if account["withdraw_number"] < withdraw_limit:
        if value >0:
            if value <= limit:
                if value <= account["balance"]:
                    account["balance"] -= value
                    account["bank_statement"] += f"Saque de R$ {value:.2f}\n"
                    print(f"Saque de R$ {value:.2f} realizado com sucesso à conta {account["account_number"]}.")
                    account["withdraw_number"] += 1
                else:
                    print(f"Lamentamos, mas o valor de saque desejado é maior que o seu saldo de R$ {account["balance"]:.2f}.")
            else:
                print(f"Lamentamos, mas você excedeu o limite de R$ {limit:.2f} por saque.")
        else:
            print("Erro. O valor a ser sacado deve ser um número maior que zero.")
    else:
        print("Lamentamos, mas você excedeu o número de saques diários")
    
    return account

def statement(*, account):
    print("\nEXTRATO DE CONTA")
    print(f"Conta de número: {account["account_number"]}")
    if account["bank_statement"] == "":
        print("Não foram realizadas movimentações")
    else:
        print(account["bank_statement"])
        print(f"\nSaldo de conta: R$ {account["balance"]:.2f}")

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
    print(f"Cliente {users[-1]["name"]} cadastrado com sucesso.")
    return users

def create_account(cpf, users, accounts):
    for user in users:
        if cpf == user["cpf"]:
            accounts.append({
                "agency": "0001",
                "account_number": len(accounts)+1,
                "user": user,
                "balance": 0,
                "bank_statement": "",
                "withdraw_number": 0
            })
            print(f"Conta número {accounts[-1]["account_number"]} cadastrada com sucesso.")
            return accounts
    print("Este CPF não foi cadastrado. Efetue o cadastro de usuário antes de cadastrar sua conta.")
    return accounts

def list_users(users):
    for user in users:
        print(f"\n CPF: {user["cpf"]} \n Nome: {user["name"]} \n Data de nascimento: {user["birth_date"]} \n Endereço: {user["address"]}")

def list_accounts(accounts):
    for account in accounts:
        print(f"\n Agência: {account["agency"]} \n Conta-corrente: {account["account_number"]} \n Cliente: {account["user"]["name"]} \n CPF: {account["user"]["cpf"]}")

class User:
    def __init__(self, address, accounts=[]):
        self._address = address
        self._accounts = accounts
    def add_account(self, account):
        self._accounts.append(account)
    def make_transaction(self, account, transaction):
        pass

class Natural_person(User):
    def __init__(self,cpf, name, birth_date, address, accounts):
        super().__init__(address, accounts)
        self._name = name
        self._cpf = cpf
        self._birth_date = birth_date

class Account:
    def __init__(self, account_number, user, statement, agency="0001", balance=0.0):
        self._agency = agency
        self._account_number = account_number
        self._user = user
        self._balance = balance
        self._statement = statement
    
    @property
    def balance(self):
        return self._balance
    
    @classmethod
    def create_account(cls, client, account_number):
        if client == None:
            print("Este CPF não foi cadastrado. Efetue o cadastro de usuário antes de cadastrar sua conta.")
        else:
            print(f"Conta número {account_number} cadastrada com sucesso.")
            return cls(agency="0001", account_number=account_number, client=client, balance=0.0, statement="")
    
    def make_deposit(self, value, /):
        if value > 0:
            self._balance += value
            self._statement += f"Depósito de R$ {value:.2f}\n"
            print(f"Depósito de R$ {value:.2f} realizado com sucesso à conta {self._account_number}")
            return True
        else:
            print("Erro. O valor a ser depositado deve ser um número maior que zero.")
            return False

    def make_withdraw(*, self, value):
        if value >0:
            if value <= self._balance:
                self._balance -= value
                self._statement += f"Saque de R$ {value:.2f}\n"
                print(f"Saque de R$ {value:.2f} realizado com sucesso à conta {self._account_number}.")
                return True
            else:
                print(f"Lamentamos, mas o valor de saque desejado é maior que o seu saldo de R$ {self._balance:.2f}.")
        else:
            print("Erro. O valor a ser sacado deve ser um número maior que zero.")
        return False

class Checking_account(Account):
    def __init__(self, account_number, user, statement, limit, withdraw_limit, agency="0001", balance=0.0):
        super().__init__(account_number, user, statement, agency, balance)
        self._limit = limit
        self._withdraw_limit = withdraw_limit
        self._withdraw_number = 0
    def make_withdraw(*, self, value):
        if self._withdraw_number < self._withdraw_limit:
            if value >0:
                if value <= self._limit:
                    if value <= self._balance:
                        self._balance -= value
                        self._statement += f"Saque de R$ {value:.2f}\n"
                        print(f"Saque de R$ {value:.2f} realizado com sucesso à conta {self._account_number}.")
                        self._withdraw_number += 1
                        return True
                    else:
                        print(f"Lamentamos, mas o valor de saque desejado é maior que o seu saldo de R$ {self._balance:.2f}.")
                else:
                    print(f"Lamentamos, mas você excedeu o limite de R$ {self._limit:.2f} por saque.")
            else:
                print("Erro. O valor a ser sacado deve ser um número maior que zero.")
        else:
            print("Lamentamos, mas você excedeu o número de saques diários")
        return False

class Transaction(ABC):
    @abstractmethod
    def register(self, account):
        pass

class Withdraw(Transaction):
    def __init__(self, value):
        self._value = value
    def register(self, account):
        pass

class Deposit(Transaction):
    def __init__(self, value):
        self._value = value
    def register(self, account):
        pass

class Statement:
    def add_transaction(self, transaction):
        pass

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
        if account_number < 1 or account_number > len(accounts):
            print("Conta-corrente não encontrada. Por favor, cadastre uma conta.")
        else:
            value = float(input("Informe o valor deseja depositar: "))
            accounts[account_number-1] = deposit(accounts[account_number-1], value)

    elif option == "s":
        account_number = int(input("Informe o número da sua conta: "))
        if account_number < 1 or account_number > len(accounts):
            print("Conta-corrente não encontrada. Por favor, cadastre cliente e conta.")
        else:
            value = float(input("Informe o valor deseja sacar: "))
            accounts[account_number-1] = withdraw(account=accounts[account_number-1], value=value, limit=limit, withdraw_limit=WITHDRAW_LIMIT)

    elif option == "e":
        account_number = int(input("Informe o número da sua conta: "))
        if account_number < 1 or account_number > len(accounts):
            print("Conta-corrente não encontrada. Por favor, cadastre cliente e conta.")
        else:
            statement(account=accounts[account_number-1])
   
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
