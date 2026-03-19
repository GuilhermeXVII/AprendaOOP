"""
Módulo 04 – Polimorfismo
=========================
Demonstramos polimorfismo com uma hierarquia de formas geométricas.
Cada forma implementa o método `area()` e `descrever()` à sua maneira,
mas podemos iterar sobre uma lista de formas e chamá-los uniformemente.
"""

import math


class Forma:
    """Classe base para formas geométricas."""

    def area(self) -> float:
        raise NotImplementedError("Subclasses devem implementar `area()`.")

    def descrever(self) -> str:
        return f"{type(self).__name__} com área = {self.area():.2f}"


class Circulo(Forma):
    def __init__(self, raio: float) -> None:
        self.raio = raio

    def area(self) -> float:
        return math.pi * self.raio ** 2


class Retangulo(Forma):
    def __init__(self, largura: float, altura: float) -> None:
        self.largura = largura
        self.altura = altura

    def area(self) -> float:
        return self.largura * self.altura


class Triangulo(Forma):
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return (self.base * self.altura) / 2


# ── Polimorfismo em ação ──────────────────────────────────────────────────────

formas = [
    Circulo(raio=5),
    Retangulo(largura=4, altura=6),
    Triangulo(base=3, altura=8),
]

print("=== Áreas das Formas ===")
for forma in formas:
    # Chamamos o mesmo método `descrever()` para objetos de tipos diferentes
    print(forma.descrever())

# Encontra a forma com maior área sem saber os tipos específicos
maior = max(formas, key=lambda f: f.area())
print(f"\nForma com maior área: {maior.descrever()}")


# ── Duck Typing ───────────────────────────────────────────────────────────────
# Nenhuma das classes abaixo herda de `Forma`, mas ambas têm `area()`.
# O Python trata qualquer objeto com `area()` da mesma forma.

class Quadrado:
    def __init__(self, lado: float) -> None:
        self.lado = lado

    def area(self) -> float:
        return self.lado ** 2

    def descrever(self) -> str:
        return f"Quadrado com área = {self.area():.2f}"


quadrado = Quadrado(lado=7)
formas.append(quadrado)   # type: ignore[arg-type]

print("\n=== Após adicionar Quadrado (Duck Typing) ===")
for forma in formas:
    print(forma.descrever())
