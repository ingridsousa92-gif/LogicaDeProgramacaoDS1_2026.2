"""
DESAFIO 06: AUDITORIA E ANÁLISE DE LOGS SUSPEITOS
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
Abra um arquivo de log, percorra suas linhas e contabilize quantas vezes
as palavras "ERROR" ou "FAIL" aparecem.
"""

# TODO: Desenvolva o script de auditoria abaixo:
# DESAFIO 06: AUDITORIA E ANÁLISE DE LOGS SUSPEITOS

nome_arquivo = "logs.txt"

contador_error = 0
contador_fail = 0

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        if "ERROR" in linha:
            contador_error += 1

        if "FAIL" in linha:
            contador_fail += 1

print("===== RELATÓRIO DE AUDITORIA =====")
print(f"Quantidade de ERROR: {contador_error}")
print(f"Quantidade de FAIL: {contador_fail}")
print(f"Total de ocorrências suspeitas: {contador_error + contador_fail}")