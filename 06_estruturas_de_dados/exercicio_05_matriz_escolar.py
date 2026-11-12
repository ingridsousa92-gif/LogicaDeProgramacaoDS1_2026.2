"""
EXERCÍCIO 05: Matriz Bidimensional Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma matriz com 3 alunos [nome, nota1, nota2].
Percorra a matriz, calcule a média de cada um e exiba:
"Aluno: [Nome] | Média: [Média] | Situação: [Aprovado / Prova Final]"
(Critério: Média >= 6.0 aprovado).
"""

# TODO: Desenvolva o algoritmo abaixo:
"""
EXERCÍCIO 05: Matriz Bidimensional Escolar
"""

# 1. Crie a matriz com 3 alunos
matriz = [
    ["Ryan", 8.0, 7.0],
    ["João", 5.0, 6.0],
    ["Maria", 9.0, 8.0]
]

# 2. Percorra a matriz e calcule as médias
for aluno in matriz:
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]

    media = (nota1 + nota2) / 2

    # 3. Verifique a situação do aluno
    if media >= 6.0:
        situacao = "Aprovado"
    else:
        situacao = "Prova Final"

    # 4. Exiba os resultados
    print(f"Aluno: {nome} | Média: {media:.1f} | Situação: {situacao}")