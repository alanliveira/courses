from __future__ import annotations

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
