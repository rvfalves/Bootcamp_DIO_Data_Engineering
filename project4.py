import textwrap, functools
from abc import ABC, abstractmethod
from datetime import datetime

def log_transaction(func):
    @functools.wraps(func)
    def envelope(*args, **kargs):
        print(f"{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} {func.__name__}")
        return func(*args, **kargs)
    return envelope

#Creating a iterator
class UserIterator:
    def __init__(self, users):
        self._users = users
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            user = self._users[self._count]
            self._count += 1
            return user
        except IndexError:
            raise StopIteration

class Client:
    def __init__(self, address):
        self._address = address
        self._accounts = []
    @property
    def accounts(self):
        return self._accounts
    
    @log_transaction
    def add_account(self, account):
        self._accounts.append(account)

    @log_transaction
    def find_account(self, account_number):
        for account in self._accounts:
            if account_number == account.account_number:
                return account
        print("Essa conta não pertence ao CPF informado.")

    def make_transaction(self, account, transaction):
        transaction.register(account)

class Natural_person(Client):
    def __init__(self, cpf, name, birth_date, address):
        super().__init__(address)
        self._name = name
        self._cpf = cpf
        self._birth_date = birth_date

    @property
    def name(self):
        return self._name
    @property
    def cpf(self):
        return self._cpf
    
    @log_transaction
    def add_user(self, users):
        for user in users:
            if self._cpf == user.cpf:
                print("Este CPF já foi cadastrado. Tente novamente.")
                return users
        users.append(self)
        print(f"Cliente {users[-1].name} cadastrado com sucesso.")
        return users
    
    def __str__(self):
        return f"""
            Cliente: {self._name}
            CPF: {self._cpf}
            Data de nascimento: {self._birth_date}
            Endereço: {self._address}
        """

class Account:
    def __init__(self, account_number, client, agency="0001", balance=0.0):
        self._agency = agency
        self._account_number = account_number
        self._client = client
        self._balance = balance
        self._history = History()
    
    @property
    def balance(self):
        return self._balance
    @property
    def account_number(self):
        return self._account_number
    @property
    def agency(self):
        return self._agency
    @property
    def client(self):
        return self._client
    @property
    def history(self):
        return self._history
    
    @classmethod 
    @log_transaction
    def create_account(cls, client, account_number):
        print(f"Conta número {account_number} cadastrada com sucesso.")
        return cls(agency="0001", account_number=account_number, client=client, balance=0.0)
    
    @log_transaction
    def make_deposit(self, value):
        if value > 0:
            self._balance += value
            print(f"Depósito de R$ {value:.2f} realizado com sucesso à conta {self._account_number}")
            return True
        else:
            print("Erro. O valor a ser depositado deve ser um número maior que zero.")
            return False
    
    @log_transaction
    def make_withdraw(self, value):
        if value >0:
            if value <= self._balance:
                self._balance -= value
                print(f"Saque de R$ {value:.2f} realizado com sucesso à conta {self._account_number}.")
                return True
            else:
                print(f"Lamentamos, mas o valor de saque desejado é maior que o seu saldo de R$ {self._balance:.2f}.")
        else:
            print("Erro. O valor a ser sacado deve ser um número maior que zero.")
        return False

class Checking_account(Account):
    def __init__(self, account_number, client, limit=500, withdraw_limit=3, agency="0001", balance=0.0):
        super().__init__(account_number, client, agency, balance)
        self._limit = limit
        self._withdraw_limit = withdraw_limit
        self._withdraw_number = 0
    def make_withdraw(self, value):
        if self._withdraw_number < self._withdraw_limit:
            if value <= self._limit:
                if super().make_withdraw(value):
                    self._withdraw_number += 1
                    return True
            else:
                print(f"Lamentamos, mas você excedeu o limite de R$ {self._limit:.2f} por saque.")
        else:
            print("Lamentamos, mas você excedeu o número de saques diários")
        return False
    def __str__(self):
        return f"""
            Agência: {self._agency}
            C/C: {self._account_number}
            Titular: {self._client.name}
            Saldo: {self._balance}
        """
    
class Transaction(ABC):
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @abstractmethod
    def register(self, account):
        pass

class Withdraw(Transaction):
    def register(self, account):
        if account.make_withdraw(self._value):
            account.history.add_transaction(self)

class Deposit(Transaction):
    def register(self, account):
        if account.make_deposit(self._value):
            account.history.add_transaction(self)

class History:
    def __init__(self):
        self._transactions = []
    
    @property
    def transactions(self):
        return self._transactions
    
    def add_transaction(self, transaction):
        self._transactions.append({"type": transaction.__class__.__name__, "value": transaction.value, "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")})
    
    #Creating a generator
    def create_report(self, transaction_type):
        for transaction in self._transactions:
            if transaction_type == None or transaction['type'].lower() == transaction_type.lower():
                yield transaction

@log_transaction
def bank_statement(account, type):
    print("\nEXTRATO DE CONTA")
    print(f"Conta de número: {account.account_number}")
    print(f"Cliente: {account.client.name}")
    
    transaction_exists = False
    statement = ""
    if type == "d":
        transaction_type = "deposit"
    elif type == "s":
        transaction_type = "withdraw"
    else:
        transaction_type = None
    
    for transaction in account.history.create_report(transaction_type):
        statement += f"\n [{transaction['date']}] - {transaction['type']}:\tR$ {transaction['value']:.2f}"
        transaction_exists = True
    if transaction_exists:
        statement += f"\nSaldo de conta: R$ {account.balance:.2f}"
    else:
        statement = "Não foram realizadas movimentações."
    print(statement)

@log_transaction
def list_users(users):
    for user in UserIterator(users):
        print(str(user))

@log_transaction
def find_user(cpf, users):
    for user in UserIterator(users):
        if cpf == user.cpf:
            return user
    print("Este CPF não foi cadastrado. Efetue o cadastro de usuário antes de cadastrar sua conta.")

@log_transaction
def list_accounts(users):
    for user in UserIterator(users):
        for account in user.accounts:
            print(str(account))

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

users=[]
account_index=0

while True:

    option = input(menu).lower()

    if option == "d":
        cpf = input("Informe o seu CPF: ")
        account_number = int(input("Informe o número da sua conta: "))
        if account_number < 1 or account_number > account_index:
            print("Conta-corrente não encontrada. Por favor, cadastre uma conta.")
        else:
            value = float(input("Informe o valor deseja depositar: "))
            client = find_user(cpf, users)
            if client != None:
                account = client.find_account(account_number)
                if account != None:
                    client.make_transaction(account, Deposit(value))

    elif option == "s":
        cpf = input("Informe o seu CPF: ")
        account_number = int(input("Informe o número da sua conta: "))
        if account_number < 1 or account_number > account_index:
            print("Conta-corrente não encontrada. Por favor, cadastre uma conta.")
        else:
            value = float(input("Informe o valor deseja sacar: "))
            client = find_user(cpf, users)
            if client != None:
                account = client.find_account(account_number)
                if account != None:
                    client.make_transaction(account, Withdraw(value))

    elif option == "e":
        cpf = input("Informe o seu CPF: ")
        account_number = int(input("Informe o número da sua conta: "))
        type = input("Informe o tipo de transações desejadas no extrato (d - apenas depósitos; s - apenas saques; c - completo): ")
        if account_number < 1 or account_number > account_index:
            print("Conta-corrente não encontrada. Por favor, cadastre uma conta.")
        else:
            client = find_user(cpf, users)
            if client != None:
                account = client.find_account(account_number)
                if account != None:
                    bank_statement(account, type)
   
    elif option == "c":
        cpf = input("Informe o seu CPF (apenas números): ")
        client = find_user(cpf, users)
        if client != None:
            account_index += 1
            new_account = Checking_account.create_account(client=client, account_number=account_index)
            client.add_account(new_account)

    elif option == "u":
        cpf = input("Informe o seu CPF (apenas números): ")
        name = input("Informe o seu nome: ")
        birth_date = input("Informe sua data de nascimento (formato DD-MM-YYYY): ")
        address = input("Informe o seu endereço (logradouro, numero - bairro - cidade/sigla estado): ")
        users = Natural_person(cpf, name, birth_date, address).add_user(users)
   
    elif option == "lc":
        list_accounts(users)

    elif option == "lu":
        list_users(users)
    
    elif option == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
