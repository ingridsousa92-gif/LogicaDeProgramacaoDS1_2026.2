"""
EXERCÍCIO 03: Adição ao Final de Arquivo (Append)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Abra o arquivo `despesas_viagem.txt` no modo 'a' e anexe uma nova linha
de despesa sem apagar o histórico anterior.
"""

# TODO: Desenvolva o algoritmo abaixo:
"""
EXERCÍCIO 03: Adição ao Final de Arquivo (Append)
"""

nome_arquivo = "despesas_viagem.txt"

nova_despesa = "Alimentação: R$ 85,00"

with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
    arquivo.write(nova_despesa + "\n")

print("Nova despesa adicionada com sucesso!")