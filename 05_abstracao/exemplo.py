"""
Módulo 05 – Abstração
======================
Usamos classes abstratas (`ABC`) para modelar diferentes meios de pagamento.
A classe abstrata `MeioDePagamento` define o contrato (interface) que todos
os meios de pagamento devem cumprir, sem implementar os detalhes.
"""

from abc import ABC, abstractmethod


class MeioDePagamento(ABC):
    """
    Classe abstrata que define o contrato para meios de pagamento.
    Não pode ser instanciada diretamente.
    """

    def __init__(self, titular: str) -> None:
        self.titular = titular

    @abstractmethod
    def pagar(self, valor: float) -> str:
        """Processa um pagamento. Deve ser implementado pelas subclasses."""
        ...

    @abstractmethod
    def descricao(self) -> str:
        """Retorna uma descrição do meio de pagamento."""
        ...

    # Método concreto: compartilhado por todas as subclasses sem necessidade de override
    def recibo(self, valor: float) -> str:
        return (
            f"--- Recibo ---\n"
            f"Titular   : {self.titular}\n"
            f"Pagamento : {self.descricao()}\n"
            f"Valor     : R$ {valor:.2f}\n"
            f"Status    : {self.pagar(valor)}\n"
            f"--------------"
        )


class CartaoDeCredito(MeioDePagamento):
    """Pagamento via cartão de crédito."""

    def __init__(self, titular: str, limite: float) -> None:
        super().__init__(titular)
        self.limite = limite
        self._gasto = 0.0

    def pagar(self, valor: float) -> str:
        if valor > (self.limite - self._gasto):
            return "RECUSADO – limite insuficiente"
        self._gasto += valor
        return "APROVADO"

    def descricao(self) -> str:
        return f"Cartão de Crédito (limite: R$ {self.limite:.2f})"


class Pix(MeioDePagamento):
    """Pagamento via Pix."""

    def __init__(self, titular: str, chave: str) -> None:
        super().__init__(titular)
        self.chave = chave

    def pagar(self, valor: float) -> str:
        return "APROVADO – transferência instantânea"

    def descricao(self) -> str:
        return f"Pix (chave: {self.chave})"


class Boleto(MeioDePagamento):
    """Pagamento via boleto bancário."""

    def pagar(self, valor: float) -> str:
        return "PENDENTE – aguardando compensação bancária (até 3 dias úteis)"

    def descricao(self) -> str:
        return "Boleto Bancário"


# ── Tentativa de instanciar a classe abstrata ─────────────────────────────────
try:
    pagamento = MeioDePagamento("Teste")  # type: ignore[abstract]
except TypeError as e:
    print(f"Erro ao instanciar classe abstrata: {e}\n")

# ── Uso polimórfico dos meios de pagamento ────────────────────────────────────

pagamentos = [
    CartaoDeCredito(titular="Ana", limite=2000.0),
    Pix(titular="Bruno", chave="bruno@email.com"),
    Boleto(titular="Carla"),
]

valores = [150.0, 300.0, 75.0]

for meio, valor in zip(pagamentos, valores):
    print(meio.recibo(valor))
    print()
