from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        conta = cls(numero, cliente)
        cliente.adicionar_conta(conta)
        return conta

    @property
    def saldo(self):
        return self._saldo

    @property 
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self._saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [t for t in self.historico.transacoes if t["tipo"] == Saque.__name__]
        )

        if valor > self.limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {self.limite:.2f}.")
        elif numero_saques >= self.limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        return f"""
Agência: {self.agencia}
C/C:     {self.numero}
Titular: {self.cliente.nome}
"""

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


def encontrar_cliente(cpf, clientes):
    for cliente in clientes:
        if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf:
            return cliente
    return None

def criar_usuario(clientes):
    cpf = input("Informe o CPF (somente números): ")
    if encontrar_cliente(cpf, clientes):
        print("Usuário já cadastrado!")
        return

    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço completo: ")

    cliente = PessoaFisica(nome, nascimento, cpf, endereco)
    clientes.append(cliente)
    print("Usuário criado com sucesso!")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = encontrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    conta = ContaCorrente.nova_conta(cliente, numero_conta)
    contas.append(conta)
    print("Conta criada com sucesso!")

def selecionar_conta(cliente):
    if not cliente.contas:
        print("Cliente não possui contas.")
        return None

    print("Contas do cliente:")
    for i, conta in enumerate(cliente.contas):
        print(f"[{i}] Conta: {conta.numero} | Saldo: R$ {conta.saldo:.2f}")

    indice = int(input("Escolha o número da conta: "))
    if 0 <= indice < len(cliente.contas):
        return cliente.contas[indice]
    else:
        print("Índice inválido.")
        return None

def listar_contas_do_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = encontrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    if not cliente.contas:
        print("Este cliente não possui contas.")
        return

    print("\nContas:")
    for conta in cliente.contas:
        print(conta)

def exibir_extrato(cliente):
    conta = selecionar_conta(cliente)
    if conta:
        print("\n=== EXTRATO ===")
        if not conta.historico.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for t in conta.historico.transacoes:
                print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
        print(f"Saldo atual: R$ {conta.saldo:.2f}")
        print("================\n")


def main():
    clientes = []
    contas = []
    numero_conta = 1

    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas do Cliente
[q] Sair
=> """

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            cpf = input("Informe o CPF do cliente: ")
            cliente = encontrar_cliente(cpf, clientes)
            if cliente:
                conta = selecionar_conta(cliente)
                if conta:
                    valor = float(input("Informe o valor do depósito: "))
                    cliente.realizar_transacao(conta, Deposito(valor))
            else:
                print("Cliente não encontrado.")

        elif opcao == "s":
            cpf = input("Informe o CPF do cliente: ")
            cliente = encontrar_cliente(cpf, clientes)
            if cliente:
                conta = selecionar_conta(cliente)
                if conta:
                    valor = float(input("Informe o valor do saque: "))
                    cliente.realizar_transacao(conta, Saque(valor))
            else:
                print("Cliente não encontrado.")

        elif opcao == "e":
            cpf = input("Informe o CPF do cliente: ")
            cliente = encontrar_cliente(cpf, clientes)
            if cliente:
                exibir_extrato(cliente)
            else:
                print("Cliente não encontrado.")

        elif opcao == "nu":
            criar_usuario(clientes)

        elif opcao == "nc":
            criar_conta(numero_conta, clientes, contas)
            numero_conta += 1

        elif opcao == "lc":
            listar_contas_do_cliente(clientes)

        elif opcao == "q":
            print("Obrigado por usar o sistema. Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()