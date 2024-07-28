#Escreva um programa em Python que conte quantas vezes cada letra 
#aparece em uma determinada palavra fornecida pelo usuário e armazene 
#essas contagens em um dicionário.

while True:
    palavra = input("Digite uma palavra: ")
    dicionario = {}

    for letra in palavra:
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1

    print("Contagem de letras na palavra:", dicionario)

    perg = input("Deseja continuar? [s/n]")
    if perg.lower() == "s":
        continue
    else:
        break


