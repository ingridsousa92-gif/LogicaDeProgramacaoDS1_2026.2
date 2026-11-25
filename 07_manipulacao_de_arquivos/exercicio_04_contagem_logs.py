"""
EXERCÍCIO 04: Contagem de Falhas em Logs
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia um arquivo de texto e conte a frequência de palavras-chave de erro
exibindo o relatório consolidado.
"""

# TODO: Desenvolva o algoritmo abaixo:
"""
EXERCÍCIO 04: Contagem de Falhas em Logs
"""

nome_arquivo = "logs.txt"

contador_error = 0
contador_fail = 0
contador_warning = 0

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if "ERROR" in linha:
                contador_error += 1

            if "FAIL" in linha:
                contador_fail += 1

            if "WARNING" in linha:
                contador_warning += 1

    print("===== RELATÓRIO DE LOGS =====")
    print(f"Erros (ERROR): {contador_error}")
    print(f"Falhas (FAIL): {contador_fail}")
    print(f"Avisos (WARNING): {contador_warning}")
    print(f"Total de ocorrências: {contador_error + contador_fail + contador_warning}")

except FileNotFoundError:
    print("ERRO: Arquivo de log não encontrado!")