"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    litros_necessarios = distancia_km / consumo_kml
    custo = litros_necessarios * preco_combustivel
    return custo


def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    custo = qtd_pessoas * dias * diaria_alimentacao
    return custo


# Programa principal
distancia = float(input("Digite a distância da viagem (km): "))
consumo = float(input("Digite o consumo do veículo (km/l): "))
preco_combustivel = float(input("Digite o preço do combustível: "))

pessoas = int(input("Digite a quantidade de pessoas: "))
dias = int(input("Digite a quantidade de dias: "))
diaria = float(input("Digite o valor da diária de alimentação por pessoa: "))


custo_transporte = calcular_custo_transporte(
    distancia, consumo, preco_combustivel
)

custo_alimentacao = calcular_custo_alimentacao(
    pessoas, dias, diaria
)

custo_total = custo_transporte + custo_alimentacao


print(f"\nCusto do transporte: R$ {custo_transporte:.2f}")
print(f"Custo da alimentação: R$ {custo_alimentacao:.2f}")
print(f"Custo total da viagem: R$ {custo_total:.2f}")

