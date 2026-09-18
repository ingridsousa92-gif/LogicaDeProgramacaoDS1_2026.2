# 1. L# TODO: Desenvolva seu algoritmo aquieia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string

valor = float(input("valor da conta:"))
pessoa = int(input("quantas pessoas há nessa mesa?"))
valor_individual = valor/pessoa
print(f"cada um vai pagar , {valor_individual:.2f}")

