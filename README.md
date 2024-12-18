# Bootcamp_DIO_Data_Engineering
 Project repository of Bootcamp DIO/NTTDATA - Data Engineering

 ## Project 1 - Description:
 "Objetivo: Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato. 
 Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.
 Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
 O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
 Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
 Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
 1500.45 = R$ 1500.45"

## Project 2 - Description:
Objetivo geral: Separar as operações existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente do banco) e cadastrar conta bancária (vincular com usuário).
Regras a seguir para as funções:
    Saque: A função saque deve receber argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.
    Depósito: A função deposito deve receber argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.
    Extrato: A função extrato deve receber argumentos por posição e nome (positional only and keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.
    Criar usuário (cliente): O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com formato: logradouro, numero - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar dois usuários com o mesmo CPF.
    Criar conta-corrente: O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta, usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de 1 conta, mas uma conta pertence apenas a 1 usuário.

## Project 3 - Description:
Objetivo geral: Iniciar modelagem do sistema bancário em POO. Adicionar classes para cliente e as operações bancárias: depósito e saque.
Atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguir o modelo de classes UML a seguir:
![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/rvf_alves/Documents/Comp/Bootcamp_Python/Projetos/Bootcamp_DIO_Data_Engineering/Trilha%20Python%20-%20desafio.png?version%3D1727097509055)
Após concluir a modelagem das classes e a criação dos métodos, atualizar os métodos que tratam as opções do menu, para funcionarem com as classes modeladas.

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

Como uma mais-valia adicional, foi proposta a criação de um arquivo de dados do tipo csv para persistir informações de usuários e conta bancária entre as chamadas do programa.  