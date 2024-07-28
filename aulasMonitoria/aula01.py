#inicie uma lista vazia ,e rode um programa que acrescente elementos nela ate que o usuario decida parar

lista = []

while True:
    elementos = input("Digite um texto qualquer: ")
    lista.append(elementos)

    perg = input("Deseja continuar? [s/n]")
    if perg == "n":
        break

for i in lista:
    print(i)