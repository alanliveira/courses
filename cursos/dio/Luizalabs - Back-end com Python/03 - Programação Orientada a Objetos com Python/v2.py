from __future__ import annotations

import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, nome: str, endereco: str):
        self.nome: str = nome
        self.endereco: str = endereco
        self.contas: list[Conta] = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento: datetime, cpf: str, endereco: str):
        super().__init__(nome, endereco)
        self.data_nascimento: datetime = data_nascimento
        self.cpf: str = cpf


class Conta:
    def __init__(self, numero: int, cliente: Cliente):
        self._saldo: float = 0
        self._numero: int = numero
        self._agencia: str = "0001"
        self._cliente: Cliente = cliente
        self._historico: Historico = Historico()

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int) -> Conta:
        return cls(numero, cliente)

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def historico(self) -> Historico:
        return self._historico

    def sacar(self, valor: float) -> bool:
        if valor < 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False

        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor: float) -> bool:
        if valor < 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        self._saldo += valor
        print("\n=== Depósito realizado com sucesso! ===")
        return True


class ContaCorrente(Conta):
    def __init__(
        self, numero: int, cliente: Cliente, limite: float = 500, limite_saque: int = 3
    ):
        super().__init__(numero, cliente)
        self.limite: float = limite
        self.limite_saque: int = limite_saque

    def sacar(self, valor: float) -> bool:
        numero_saque = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        if valor > self.limite:
            print("\n@@@ Operação falhou! O valor do saque excedeu o limite. @@@")
            return False

        if numero_saque >= self.limite_saque:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False

        return super().sacar(valor)

    def __str__(self):
        return f"""\
Agência:\t{self.agencia}
C/C:\t{self.numero}
Titular:\t{self.cliente.nome}
"""


class Historico:
    def __init__(self):
        self._transacoes: list[dict] = []

    @property
    def transacoes(self) -> list[dict]:
        return list(self._transacoes)

    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now(),
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self) -> float:
        pass

    @abstractmethod
    def registrar(self, conta: Conta) -> None:
        pass


class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor: float = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta: Conta) -> None:
        sucesso_transacao = conta.sacar(self._valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor: float = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta: Conta) -> None:
        sucesso_transacao = conta.depositar(self._valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


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


def _ler_valor(mensagem: str) -> float | None:
    """Lê um valor monetário informado pelo usuário"""
    try:
        return float(input(mensagem))
    except ValueError:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return None


def _filtrar_usuario(cpf: str, clientes: list[PessoaFisica], /) -> PessoaFisica | None:
    """Filtra os usuários do sistema"""
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def _filtrar_conta(contas: list[Conta], /) -> Conta | None:
    """Filtra a conta que será utilizada na operação"""
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada! @@@")
        return None

    try:
        numero_conta = int(input("Informe o número da conta: "))
    except ValueError:
        print("\n@@@ Operação falhou! O número da conta é inválido. @@@")
        return None

    conta = next(
        (conta for conta in contas if conta.numero == numero_conta),
        None,
    )

    if not conta:
        print("\n@@@ Conta não encontrada! @@@")

    return conta


def depositar(conta: Conta, /) -> None:
    """Realiza um depósito na conta"""
    print("================ Depósito ================")
    valor = _ler_valor("Informe o valor do depósito: ")

    if valor is None:
        return

    if valor <= 0:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return

    conta.cliente.realizar_transacao(conta, Deposito(valor))


def sacar(conta: Conta, /) -> None:
    """Realiza o saque da conta"""
    print("================ Saque ================")
    valor = _ler_valor("Informe o valor do saque: ")

    if valor is None:
        return

    if valor <= 0:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return

    conta.cliente.realizar_transacao(conta, Saque(valor))


def exibir_extrato(conta: Conta, /) -> None:
    """Exibe o extrato da conta"""
    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in transacoes:
            tipo = (
                "Depósito"
                if transacao["tipo"] == Deposito.__name__
                else transacao["tipo"]
            )
            print(f"{tipo}: R$ {transacao['valor']:.2f}")

    print(f"\nSaldo:\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_usuario(clientes: list[PessoaFisica], /) -> None:
    """Cria um novo usuário"""
    print("================ Criar usuário ================")
    cpf = input("Informe o CPF (somente número): ")
    cliente = _filtrar_usuario(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o seu endereço (logradouro, nro - bairro, cidade/Sigla estado): "
    )

    try:
        data = datetime.strptime(data_nascimento, "%d-%m-%Y")
    except ValueError:
        print("\n@@@ Operação falhou! A data informada é inválida. @@@")
        return

    clientes.append(
        PessoaFisica(nome=nome, data_nascimento=data, cpf=cpf, endereco=endereco)
    )

    print("=== usuário criado com sucesso! ===")


def criar_conta(
    numero_conta: int, clientes: list[PessoaFisica], /
) -> ContaCorrente | None:
    """Cria uma nova conta associada ao usuário"""
    print("================ Criar conta ================")
    cpf = input("Informe o CPF do usuário: ")
    cliente = _filtrar_usuario(cpf, clientes)

    if not cliente:
        print("\n@@@ Usuário não encontrado! @@@")
        return None

    conta = ContaCorrente.nova_conta(cliente, numero_conta)
    cliente.adicionar_conta(conta)
    print("\n=== Conta criada com sucesso! ===")
    return conta


def listar_contas(contas: list[Conta]) -> None:
    """Lista todas as contas criadas no sistema"""
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada! @@@")
        return

    for conta in contas:
        print("=" * 100)
        print(conta, end="")


def main() -> None:
    """Controle do sistema"""
    clientes: list[PessoaFisica] = []
    contas: list[Conta] = []

    while True:
        opcao = menu()

        match opcao:
            case "d":
                conta = _filtrar_conta(contas)

                if conta:
                    depositar(conta)
            case "s":
                conta = _filtrar_conta(contas)

                if conta:
                    sacar(conta)
            case "e":
                conta = _filtrar_conta(contas)

                if conta:
                    exibir_extrato(conta)
            case "nu":
                criar_usuario(clientes)
            case "nc":
                numero_conta: int = len(contas) + 1
                conta = criar_conta(numero_conta, clientes)

                if conta:
                    contas.append(conta)
            case "lc":
                listar_contas(contas)
            case "q":
                break
            case _:
                print(
                    "\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@"
                )


if __name__ == "__main__":
    main()
