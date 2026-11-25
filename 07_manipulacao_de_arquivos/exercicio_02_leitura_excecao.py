"""
EXERCÍCIO 02: Leitura com Tratamento de Exceção
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Tente ler o arquivo `dados_iniciais_casas_paulino.csv`.
Trate a exceção FileNotFoundError com try-except exibindo alerta amigável.
"""

# TODO: Desenvolva o algoritmo abaixo:
"""
EXERCÍCIO 02: Leitura com Tratamento de Exceção
"""

nome_arquivo = "dados_iniciais_casas_paulino.csv"

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("Arquivo lido com sucesso!")
        print(conteudo)

except FileNotFoundError:
    print("ATENÇÃO: O arquivo não foi encontrado!")
    print("Verifique se o nome e o local do arquivo estão corretos.")