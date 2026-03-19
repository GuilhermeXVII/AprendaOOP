# Módulo 01 – Classes e Objetos

## O que é uma Classe?

Uma **classe** é um molde (ou modelo) que define as características e comportamentos de um tipo de objeto.
Pense em uma classe como a planta de uma casa: ela descreve como a casa será construída, mas não é a casa em si.

## O que é um Objeto?

Um **objeto** é uma instância de uma classe — a "casa" construída a partir da planta.
Cada objeto pode ter valores próprios para seus atributos, mas todos seguem a estrutura definida pela classe.

## Anatomia de uma Classe em Python

```python
class NomeDaClasse:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1   # atributo de instância
        self.atributo2 = atributo2

    def meu_metodo(self):
        # comportamento do objeto
        pass
```

- `__init__`: método construtor, executado automaticamente ao criar um objeto.
- `self`: referência ao próprio objeto; sempre é o primeiro parâmetro dos métodos de instância.

## Execute o exemplo

```bash
python 01_classes_e_objetos/exemplo.py
```
