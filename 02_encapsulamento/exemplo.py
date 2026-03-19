"""
Módulo 02 – Encapsulamento
===========================
Modelamos uma conta bancária simples onde o saldo é protegido:
- Não pode ser alterado diretamente (sem validação).
- Depósitos e saques passam por regras de negócio.
"""


class ContaBancaria:
    """Conta bancária com saldo encapsulado."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0) -> None:
        self.titular = titular          # público
        self._saldo = saldo_inicial     # protegido (convenção)

    # ── Getter ────────────────────────────────────────────────────────────────

    @property
    def saldo(self) -> float:
        """Retorna o saldo atual (somente leitura via property)."""
        return self._saldo

    # ── Métodos de negócio ────────────────────────────────────────────────────

    def depositar(self, valor: float) -> None:
        """Adiciona valor ao saldo, validando que seja positivo."""
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._saldo += valor
        print(f"[+] Depósito de R$ {valor:.2f} realizado. Saldo atual: R$ {self._saldo:.2f}")

    def sacar(self, valor: float) -> None:
        """Remove valor do saldo, validando que seja positivo e que haja saldo suficiente."""
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor
        print(f"[-] Saque de R$ {valor:.2f} realizado. Saldo atual: R$ {self._saldo:.2f}")

    def extrato(self) -> str:
        """Retorna um extrato resumido da conta."""
        return f"Titular: {self.titular} | Saldo: R$ {self._saldo:.2f}"


# ── Uso da classe ─────────────────────────────────────────────────────────────

conta = ContaBancaria(titular="Alice", saldo_inicial=500.0)

print(conta.extrato())
conta.depositar(200.0)
conta.sacar(100.0)
print(conta.extrato())

# Tentando acessar o saldo diretamente via property (somente leitura)
print(f"\nSaldo via property: R$ {conta.saldo:.2f}")

# Tentando um saque inválido
try:
    conta.sacar(1000.0)
except ValueError as e:
    print(f"\nErro: {e}")
