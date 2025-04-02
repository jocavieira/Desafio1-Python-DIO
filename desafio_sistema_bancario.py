def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = next((user for user in usuarios if user["cpf"] == cpf), None)
    
    if usuario:
        print("ERRO!\nUsuário já cadastrado!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")
    
    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")


def criar_conta(agencia, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((user for user in usuarios if user["cpf"] == cpf), None)

    if not usuario:
        print("ERRO!\nUsuário não encontrado! Criação de conta falhou.")
        return

    # Filtrar contas do usuário e determinar o próximo número de conta
    contas_usuario = [conta for conta in contas if conta["usuario"]["cpf"] == cpf]
    numero_conta = len(contas_usuario) + 1  # Contagem começa de 1 para cada usuário
    conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    contas.append(conta)

    print(f"Conta criada com sucesso! Agência: {agencia}, Número da Conta: {numero_conta}")



def main():
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    numero_conta = 1
    
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [q] Sair
    => """
    
    while True:
        opcao = input(menu)
        
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            criar_conta(AGENCIA, usuarios, contas)
        
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema. Até mais!")
            break
        
        else:
            print("Operação inválida! Selecione uma opção válida.")


if __name__ == "__main__":
    main()
