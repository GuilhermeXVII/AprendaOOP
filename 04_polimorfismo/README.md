# Módulo 04 – Polimorfismo

## O que é Polimorfismo?

**Polimorfismo** (do grego: "muitas formas") é a capacidade de diferentes objetos responderem ao mesmo método de maneiras diferentes.

Em Python, o polimorfismo é natural: se dois objetos têm um método com o mesmo nome, você pode chamá-los de forma uniforme sem se preocupar com o tipo de cada um.

## Tipos de Polimorfismo

### 1. Polimorfismo por Herança (Method Overriding)
A subclasse sobrescreve um método da superclasse, fornecendo sua própria implementação.

### 2. Duck Typing
"Se anda como um pato e grasna como um pato, então é um pato."
Em Python, o que importa é o objeto ter o método esperado, não de qual classe ele veio.

## Por que isso é útil?

Permite escrever código genérico que funciona com qualquer objeto que implemente determinada interface, sem precisar verificar o tipo explicitamente.

```python
for animal in lista_de_animais:
    print(animal.fazer_som())   # funciona para qualquer animal
```

## Execute o exemplo

```bash
python 04_polimorfismo/exemplo.py
```
