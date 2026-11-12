"""
EXERCÍCIO 01: Lista de Monitores
Disciplina: Lógica de Programação com Python

ENUNCIADO:
1. Crie uma lista com o primeiro monitor: "Ryan Mesquita Damasceno".
2. Adicione 2 novos monitores com .append().
3. Demonstre a mutabilidade alterando o nome na posição 0.
4. Imprima a lista final.
"""

# TODO: Desenvolva o algoritmo abaixo:
"""
EXERCÍCIO 01: Lista de Monitores
"""

# 1. Crie uma lista com o primeiro monitor
monitores = ["Ryan Mesquita Damasceno"]

# 2. Adicione 2 novos monitores
monitores.append("João Silva")
monitores.append("Maria Oliveira")

# 3. Altere o nome na posição 0
monitores[0] = "Ryan Mesquita"

# 4. Imprima a lista final
print(monitores)