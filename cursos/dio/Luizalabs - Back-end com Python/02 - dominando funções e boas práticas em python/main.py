import textwrap
from datetime import date
from typing import TypedDict

class Usuario(TypedDict):
    nome: str
    data_nascimento: date
    cpf: str
    endereco: str

class Conta(TypedDict):
    agencia: str
    numero_conta: int
    usuario: Usuario

def menu() -> str:
    menu = """
    ================ Menu ================

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo: float, valor: float, extrato: float, /) -> tuple[float, float]:
    """Realizar um depósito na conta"""
    print("================ Depósito ================")
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== depósito realizado com sucesso ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def sacar(*, saldo: float, valor: float, extrato: float, limite: float, numero_saques: int, limite_saques: int) -> tuple[float, float]:
    """Realizar o saque da conta"""
    print("================ Saque ================")
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@ ")

    return saldo, extrato

def exibir_extrato(saldo: float, /, *, extrato: float):
    """Exibe o extrato da conta"""
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios: list[Usuario], /) -> None:
    """Cria um novo usuário"""
    print("================ Criar usuário ================")
    cpf: str = input("Informe o CPF (somente número): ")
    usuario: Usuario | None = _filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (logradouro, nro - bairro, cidade/Sigla estado): ")

    usuarios.append(Usuario(nome=nome, data_nascimento=date.strptime(data_nascimento, "%d-%m-%Y"), endereco=endereco, cpf=cpf))

    print("=== usuários criado com sucesso! ===")

def _filtrar_usuario(cpf:str, usuarios: list[Usuario], /) -> Usuario | None:
    """Filtra os usuários do sistema"""
    usuarios_filtratos = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtratos[0] if usuarios_filtratos else None

def criar_conta(agencia: str, numero_conta: int, usuarios: list[Usuario]) -> Conta | None:
    """Cria uma nova conta associada ao usuário"""
    cpf: str = input("Informe o CPF do usuário: ")
    usuario = _filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return Conta(agencia=agencia, numero_conta=numero_conta, usuario=usuario)

def listar_contas(contas: list[Conta]) -> None:
    """Lista todas as contas criadas no sistema"""
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main() -> None:
    """Controle do sistema"""
    
    saldo: float = 0
    limite: int = 500
    extrato: str = ""
    numero_saques: int = 0
    LIMITE_SAQUES: int = 3

    usuarios: list[Usuario] = []
    contas: list[Conta] = []
    AGENCIA: str = "0000"

    while True:
        opcao = menu()

        match(opcao):
            case "d":
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)
            case "s":
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
                )
            case "e":
                exibir_extrato(saldo, extrato=extrato)
            case "nu":
                criar_usuario(usuarios)
            case "nc":
                numero_conta: int = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)
            case "lc":
                listar_contas(contas)
            case "q":
                break
            case _:
                print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

if __name__ == "__main__":
    main()