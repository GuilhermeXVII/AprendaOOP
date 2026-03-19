"""
Módulo 03 – Herança
====================
Modelamos uma hierarquia de funcionários de uma empresa:

    Funcionario          ← classe base (pai)
    ├── Desenvolvedor    ← especialização com linguagem favorita
    └── Gerente          ← especialização com número de subordinados

Comportamentos comuns ficam em `Funcionario`; cada subclasse
adiciona ou sobrescreve apenas o que é específico para ela.
"""


class Funcionario:
    """Representa um funcionário genérico da empresa."""

    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    def apresentar(self) -> str:
        return f"Funcionário: {self.nome} | Salário: R$ {self.salario:.2f}"

    def conceder_aumento(self, percentual: float) -> None:
        """Aplica um aumento percentual ao salário."""
        self.salario *= 1 + percentual / 100
        print(f"Aumento de {percentual}% concedido a {self.nome}. Novo salário: R$ {self.salario:.2f}")


class Desenvolvedor(Funcionario):
    """Funcionário especializado em desenvolvimento de software."""

    def __init__(self, nome: str, salario: float, linguagem: str) -> None:
        super().__init__(nome, salario)   # reutiliza o __init__ do pai
        self.linguagem = linguagem

    # Sobrescreve (override) o método da classe pai para adicionar mais detalhes
    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} | Linguagem: {self.linguagem}"


class Gerente(Funcionario):
    """Funcionário com responsabilidades de gestão."""

    def __init__(self, nome: str, salario: float, n_subordinados: int) -> None:
        super().__init__(nome, salario)
        self.n_subordinados = n_subordinados

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} | Subordinados: {self.n_subordinados}"

    def realizar_reuniao(self) -> str:
        return f"{self.nome} está realizando uma reunião com {self.n_subordinados} subordinado(s)."


# ── Uso das classes ───────────────────────────────────────────────────────────

dev = Desenvolvedor(nome="Carlos", salario=8000.0, linguagem="Python")
gerente = Gerente(nome="Beatriz", salario=15000.0, n_subordinados=5)

print(dev.apresentar())
print(gerente.apresentar())

print()

# Comportamento herdado da classe pai
dev.conceder_aumento(10)
gerente.conceder_aumento(5)

print()

# Comportamento exclusivo da subclasse
print(gerente.realizar_reuniao())

# Verificando a hierarquia de herança
print()
print(f"dev é instância de Funcionario? {isinstance(dev, Funcionario)}")
print(f"dev é instância de Desenvolvedor? {isinstance(dev, Desenvolvedor)}")
print(f"dev é instância de Gerente? {isinstance(dev, Gerente)}")
