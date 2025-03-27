# Sistema Bancário em Python

## Descrição do Projeto
Este projeto consiste no desenvolvimento de um sistema bancário simples utilizando a linguagem Python. O objetivo é fornecer as funcionalidades básicas de um banco, permitindo que o usuário realize operações de **depósito**, **saque** e **exibição de extrato**.

O sistema foi projetado para atender aos requisitos de um banco fictício que deseja modernizar suas operações. Como essa é a primeira versão do sistema, apenas um usuário é suportado e não há necessidade de identificação de agência ou conta bancária.

## Funcionalidades Implementadas
O sistema permite que o usuário execute as seguintes operações:

### 1. **Depósito**
- O usuário pode depositar valores positivos na conta.
- Os depósitos são armazenados e exibidos na operação de extrato.

### 2. **Saque**
- O usuário pode realizar até **3 saques diários**.
- O valor máximo por saque é de **R$ 500,00**.
- Caso o usuário tente sacar mais do que o saldo disponível, uma mensagem de erro será exibida.
- Todos os saques são armazenados e exibidos na operação de extrato.

### 3. **Extrato**
- Exibe todos os depósitos e saques realizados pelo usuário.
- No final da listagem, exibe o saldo atual da conta.
- Caso não haja movimentações, exibe a mensagem: **"Não foram realizadas movimentações."**
- Todos os valores são exibidos no formato **R$ xxx.xx**.

## Estrutura do Código
O código foi modularizado em funções para facilitar a manutenção e organização:
- `depositar(saldo, extrato)`: Realiza depósitos na conta.
- `sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)`: Permite que o usuário saque dinheiro seguindo as regras do sistema.
- `exibir_extrato(saldo, extrato)`: Exibe todas as transações realizadas pelo usuário.
- `main()`: Função principal que executa o menu interativo do sistema.

## Tecnologias Utilizadas
- Linguagem: **Python 3**
- Conceitos utilizados: **Estruturas de controle (if/else, loops), funções, manipulação de strings e listas**.

## Melhorias Futuras
- Implementação de múltiplos usuários com identificação de conta.
- Integração com banco de dados para persistência de dados.
- Interface gráfica para melhorar a experiência do usuário.

