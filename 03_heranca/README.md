# Módulo 03 – Herança

## O que é Herança?

**Herança** permite que uma classe (chamada de **subclasse** ou classe filha) herde atributos e métodos de outra classe (chamada de **superclasse** ou classe pai).

Isso promove:
- **Reutilização de código**: comportamentos comuns são definidos uma única vez na classe pai.
- **Especialização**: cada subclasse pode adicionar ou sobrescrever comportamentos.

## Sintaxe em Python

```python
class Pai:
    def saudacao(self):
        return "Olá da classe Pai!"

class Filho(Pai):           # Filho herda de Pai
    def saudacao(self):     # Sobrescreve (override) o método da classe pai
        return "Olá da classe Filho!"
```

## `super()`

A função `super()` permite chamar métodos da classe pai dentro da subclasse, evitando duplicação de código — especialmente útil no `__init__`.

```python
class Filho(Pai):
    def __init__(self, nome, turma):
        super().__init__(nome)   # chama o __init__ do Pai
        self.turma = turma
```

## Execute o exemplo

```bash
python 03_heranca/exemplo.py
```
