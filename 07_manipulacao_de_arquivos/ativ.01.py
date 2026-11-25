# TODO: Implemente a escrita dos 3 softwares no arquivo
nome_arquivo = "meus_softwares.txt"

# Escreva a lógica com with open(...)
softwares = ["Python", "Visual Studio Code", "Git"]

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    for software in softwares:
        arquivo.write(software + "\n")