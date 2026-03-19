"""
Módulo 01 – Classes e Objetos
==============================
Neste exemplo criamos a classe `Cachorro` para representar um cachorro.
Cada cachorro tem seu próprio nome e raça, mas todos "sabem" latir e se apresentar.
"""


class Cachorro:
    """Representa um cachorro com nome e raça."""

    # Atributo de classe: compartilhado por todos os objetos da classe
    especie = "Canis lupus familiaris"

    def __init__(self, nome: str, raca: str) -> None:
        """Inicializa o cachorro com nome e raça."""
        # Atributos de instância: exclusivos de cada objeto
        self.nome = nome
        self.raca = raca

    def latir(self) -> str:
        """Retorna o som do latido."""
        return "Au au!"

    def apresentar(self) -> str:
        """Retorna uma apresentação completa do cachorro."""
        return (
            f"Olá! Meu nome é {self.nome}, "
            f"sou da raça {self.raca} "
            f"e pertenço à espécie {self.especie}."
        )


# ── Criando objetos (instâncias) ──────────────────────────────────────────────

rex = Cachorro(nome="Rex", raca="Pastor Alemão")
bolinha = Cachorro(nome="Bolinha", raca="Poodle")

# Cada objeto tem seus próprios dados
print(rex.apresentar())
print(bolinha.apresentar())

# Ambos compartilham o mesmo comportamento
print(f"{rex.nome} diz: {rex.latir()}")
print(f"{bolinha.nome} diz: {bolinha.latir()}")

# O atributo de classe é o mesmo para todos
print(f"\nEspécie: {Cachorro.especie}")
