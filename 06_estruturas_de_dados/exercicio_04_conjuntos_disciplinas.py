"""
EXERCÍCIO 04: Conjuntos (Set) de Disciplinas
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie 2 sets de estudantes (alunos_web e alunos_banco).
Calcule e imprima a Interseção (&) e a Diferença (-).
"""

# TODO: Desenvolva o algoritmo abaixo:
"""
EXERCÍCIO 04: Conjuntos (Set) de Disciplinas
"""

# 1. Crie 2 sets de estudantes
alunos_web = {"Ryan", "João", "Maria", "Pedro"}

alunos_banco = {"Ryan", "Maria", "Ana", "Carlos"}

# 2. Calcule a interseção (&)
intersecao = alunos_web & alunos_banco

# 3. Calcule a diferença (-)
diferenca = alunos_web - alunos_banco

# 4. Imprima os resultados
print("Interseção:", intersecao)
print("Diferença:", diferenca)