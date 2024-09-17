# Bootcamp_DIO_Data_Engineering
 Project repository of Bootcamp DIO/NTTDATA - Data Engineering

 Project 1 - Description:
 "Objetivo: Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato. 
 Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.
 Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
 O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
 Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
 Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
 1500.45 = R$ 1500.45"

Project 2 - Description:
Objetivo geral: Seperar as operações existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente do banco) e cadastrar conta bancária (vincular com usuário).
Regras a seguir para as funções:
    Saque: A função saque deve receber argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.
    Depósito: A função deposito deve receber argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.
    Extrato: A função extrato deve receber argumentos por posição e nome (positional only and keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.
    Criar usuário (cliente): O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com formato: logradouro, numeoro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar dois usuários com o mesmo CPF.
    Criar conta-corrente: O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta, usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de 1 conta, mas uma conta pertence apenas a 1 usuário.