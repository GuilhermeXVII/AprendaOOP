# Módulo 02 – Encapsulamento

## O que é Encapsulamento?

**Encapsulamento** é o princípio de proteger os dados de um objeto, controlando como eles são lidos ou modificados.
O objetivo é garantir que o estado interno do objeto só seja alterado de formas seguras e controladas.

## Convenções em Python

Python usa convenções de nomenclatura para indicar o nível de acesso:

| Prefixo | Exemplo | Significado |
|---------|---------|-------------|
| sem prefixo | `self.nome` | Público – acessível de qualquer lugar |
| `_` simples | `self._saldo` | Protegido – convenção; não acesse diretamente fora da classe |
| `__` duplo | `self.__senha` | Privado (name mangling) – dificulta acesso externo acidental |

## Getters e Setters com `@property`

A maneira pythônica de criar getters e setters é usando o decorador `@property`.
Isso permite validar os dados antes de salvá-los, mantendo uma interface limpa.

```python
@property
def saldo(self):
    return self._saldo

@saldo.setter
def saldo(self, valor):
    if valor < 0:
        raise ValueError("Saldo não pode ser negativo")
    self._saldo = valor
```

## Execute o exemplo

```bash
python 02_encapsulamento/exemplo.py
```
