# Sistema Bancário em Python

## Descrição do Projeto
Este projeto consiste no desenvolvimento de um sistema bancário simples utilizando a linguagem Python. O objetivo é fornecer as funcionalidades básicas de um banco, permitindo que os usuários realizem operações de **depósito**, **saque**, **exibição de extrato** e **criação de contas bancárias**.

O sistema foi projetado para atender aos requisitos de um banco fictício, permitindo que múltiplos usuários criem contas associadas a seu CPF e realizem transações bancárias. As funcionalidades incluem:


### 1. **Criação de Usuário**
- O usuário pode ser cadastrado no sistema informando seu **nome**, **data de nascimento**, **CPF** e **endereço**.
- O CPF é utilizado como identificador único para cada usuário, não permitindo duplicidade.

### 2. **Criação de Conta**
- Para cada usuário, pode ser criada uma ou mais contas bancárias.
- O número da conta é sequencial para cada novo usuário e começa sempre de **1**.
- O número da agência é fixo: **0001**.
  
### 3. **Depósito**
- O usuário pode realizar depósitos na sua conta.
- Os depósitos são registrados e aparecem no extrato.
- O valor do depósito deve ser positivo.

### 4. **Saque**
- O usuário pode realizar até **3 saques diários**.
- O valor máximo por saque é de **R$ 500,00**.
- Caso o usuário tente sacar mais do que o saldo disponível ou ultrapasse os limites, uma mensagem de erro será exibida.
- Todos os saques realizados são registrados e exibidos no extrato.

### 5. **Extrato**
- Exibe todas as transações realizadas pelo usuário, incluindo **depósitos** e **saques**.
- Ao final do extrato, é exibido o **saldo atual** da conta.
- Se o usuário não realizar nenhuma transação, será exibida a mensagem: **"Não foram realizadas movimentações."**
- Todos os valores são exibidos no formato **R$ xxx.xx**.

## Estrutura do Código
O código foi modularizado para facilitar a manutenção e organização das funcionalidades. As principais classes e funções são:

### **Classes**
- `Cliente`: Representa um cliente, contendo o endereço e as contas associadas.
- `PessoaFisica`: Subclasse de `Cliente` que adiciona informações específicas para pessoas físicas, como nome, data de nascimento e CPF.
- `Conta`: Representa uma conta bancária, com funcionalidades para **sacar**, **depositar** e acessar o **saldo** e **histórico** de transações.
- `ContaCorrente`: Subclasse de `Conta` que adiciona limites de saque e um número máximo de saques diários.
- `Historico`: Armazena as transações realizadas nas contas.
- `Transacao`: Classe base para transações, como **Saque** e **Depósito**.
- `Saque`: Representa um saque realizado, com verificação de saldo e limite de saque.
- `Deposito`: Representa um depósito realizado, com verificação de valor válido.

### **Funções**
- `encontrar_cliente(cpf, clientes)`: Encontra um cliente no sistema pelo CPF.
- `criar_usuario(clientes)`: Cria um novo usuário com as informações fornecidas (nome, data de nascimento, CPF e endereço).
- `criar_conta(numero_conta, clientes, contas)`: Cria uma nova conta bancária para um usuário existente, com número de conta sequencial.
- `selecionar_conta(cliente)`: Permite ao cliente selecionar uma das suas contas para realizar transações.
- `listar_contas_do_cliente(clientes)`: Lista todas as contas de um cliente.
- `exibir_extrato(cliente)`: Exibe o extrato da conta do cliente com todas as transações realizadas.
- `main()`: Função principal que executa o menu interativo do sistema e gerencia as operações.
