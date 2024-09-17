menu = """

Escolha a operação de deseja executar:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

balance = 0
limit = 500
bank_statement = ""
withdraw_number = 0
WITHDRAW_LIMIT = 3

while True:

    option = input(menu)

    if option == "d":
        deposit = float(input("Informe o valor deseja depositar: "))
        if deposit > 0:
            balance += deposit
            bank_statement += f"Depósito de R$ {deposit:.2f}\n"
            print(f"Depósito de R$ {deposit:.2f} realizado com sucesso.")
        else:
            print("Erro. O valor a ser depositado deve ser um número maior que zero.")

    elif option == "s":
        if withdraw_number < WITHDRAW_LIMIT:
            withdraw = float(input("Informe o valor deseja sacar: "))
            if withdraw >0:
                if withdraw <= limit:
                    if withdraw <= balance:
                        balance -= withdraw
                        bank_statement += f"Saque de R$ {withdraw:.2f}\n"
                        print(f"Saque de R$ {withdraw:.2f} realizado com sucesso.")
                        withdraw_number += 1
                    else:
                        print(f"Lamentamos, mas o valor de saque desejado é maior que o seu saldo de R$ {balance:.2f}.")
                else:
                    print(f"Lamentamos, mas você excedeu o limite de R$ {limit:.2f} por saque.")
            else:
                print("Erro. O valor a ser sacado deve ser um número maior que zero.")
        else:
            print("Lamentamos, mas você excedeu o número de saques diários")

    elif option == "e":
       print("\nEXTRATO DE CONTA")
       if bank_statement == "":
           print("Não foram realizadas movimentações")
       else:
           print(bank_statement)
           print(f"\nSaldo de conta: R$ {balance:.2f}")

    elif option == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")