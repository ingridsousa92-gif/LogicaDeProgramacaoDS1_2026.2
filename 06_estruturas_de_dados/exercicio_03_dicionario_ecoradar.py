"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Estruture um dicionário com 3 membros (matrícula -> cargo).
Leia uma matrícula via terminal e exiba a função correspondente cadastrada.
"""

# TODO: Desenvolva o algoritmo abaixo:
"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
"""

# 1. Crie o dicionário com 3 membros
equipe = {
    "101": "Coordenador",
    "102": "Pesquisador",
    "103": "Analista"
}

# 2. Leia uma matrícula pelo terminal
matricula = input("Digite sua matrícula: ")

# 3. Exiba o cargo correspondente
cargo = equipe.get(matricula)

if cargo:
    print("Cargo cadastrado:", cargo)
else:
    print("Matrícula não encontrada!")