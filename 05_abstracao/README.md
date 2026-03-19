# Módulo 05 – Abstração

## O que é Abstração?

**Abstração** é o processo de modelar apenas os aspectos relevantes de uma entidade do mundo real, ocultando complexidades desnecessárias.

Em termos práticos, uma classe abstrata define **o quê** deve ser feito (a interface), mas deixa para as subclasses a responsabilidade de definir **como** fazer.

## Classes Abstratas em Python

Python oferece o módulo `abc` (Abstract Base Classes) para criar classes abstratas:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self) -> str:
        """Cada animal deve implementar seu próprio som."""
        ...
```

- Uma classe que herda de `ABC` **não pode ser instanciada** diretamente.
- Subclasses **são obrigadas** a implementar todos os métodos marcados com `@abstractmethod`.

## Por que usar Abstração?

- Define **contratos**: garante que toda subclasse implemente os métodos necessários.
- Facilita o **polimorfismo**: permite tratar objetos distintos de forma uniforme.
- Melhora a **manutenibilidade**: mudanças na interface ficam centralizadas.

## Execute o exemplo

```bash
python 05_abstracao/exemplo.py
```
