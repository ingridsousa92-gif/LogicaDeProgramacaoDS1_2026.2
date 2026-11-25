"""
EXERCÍCIO 01: Gerenciador de Contexto e Log de Rede
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Use `with open("acessos_laboratorio.txt", "w")` para criar e salvar
os horários de entrada e saída de 3 turmas no laboratório.
"""

# TODO: Desenvolva o algoritmo abaixo:

"""
EXERCÍCIO 01: Gerenciador de Contexto e Log de Rede
"""

nome_arquivo = "acessos_laboratorio.txt"

turmas = [
    "Turma 1 - Entrada: 07:00 | Saída: 09:00",
    "Turma 2 - Entrada: 09:00 | Saída: 11:00",
    "Turma 3 - Entrada: 13:00 | Saída: 15:00"
]

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    for turma in turmas:
        arquivo.write(turma + "\n")

print("Horários das 3 turmas salvos com sucesso!")