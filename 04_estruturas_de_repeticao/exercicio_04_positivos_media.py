"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
soma = 0
contador = 0

for i in range(6):
    numero = float(input("Digite um valor: "))

    if numero > 0:
        soma += numero
        contador += 1

if contador > 0:
    media = soma / contador
else:
    media = 0

print(f"{contador} valores positivos")
print(f"Média: {media:.1f}")

