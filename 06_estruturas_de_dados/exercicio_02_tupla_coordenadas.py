"""
EXERCÍCIO 02: Tupla de Coordenadas e Imutabilidade
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma tupla com as cidades ("Tianguá", "São Benedito").
Tente alterar a posição 1 e use try-except para capturar o TypeError,
exibindo uma mensagem explicativa sobre imutabilidade.
"""

# TODO: Desenvolva o algoritmo abaixo:
"""
EXERCÍCIO 02: Tupla de Coordenadas e Imutabilidade
"""

# 1. Crie a tupla com as cidades
cidades = ("Tianguá", "São Benedito")

# 2. Tente alterar a posição 1
try:
    cidades[1] = "Fortaleza"

except TypeError:
    print("Erro: Não é possível alterar uma tupla, pois ela é imutável!")

# 3. Exiba a tupla original
print(cidades)