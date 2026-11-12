"""
DESAFIO 05: O INVENTÁRIO SUSPEITO DO LABORATÓRIO
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
Elimine duplicatas usando conjuntos (set) e previna o erro KeyError em dicionários
usando o método .get().

SUA MISSÃO:
1. Obtenha a lista de itens únicos a partir de uma lista com duplicatas.
2. Consulte chaves no dicionário de forma segura sem quebrar o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:
"""
DESAFIO 05: O INVENTÁRIO SUSPEITO DO LABORATÓRIO
"""

# Lista de itens com duplicatas
itens = ["Microscópio", "Tubo de ensaio", "Microscópio", "Luvas", "Luvas"]

# 1. Eliminar duplicatas usando set
itens_unicos = set(itens)

print("Itens únicos:", itens_unicos)

# Criando um dicionário
inventario = {
    "Microscópio": 5,
    "Tubo de ensaio": 10,
    "Luvas": 20
}

# 2. Consultar chaves usando .get()
print("Quantidade de microscópios:", inventario.get("Microscópio"))
print("Quantidade de reagentes:", inventario.get("Reagentes", 0))