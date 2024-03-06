from random import choice

senha = []
caracterLetra = 'abcdefghijklmnopqrstuvxzyw'
caracter_Num = '1234567890#ç$@!'


numero = int(input("Digite a qnt de caracteres:"))

escolha = input('Voce deseja fazer uma senha:\n1-somente letras\n2-somente numeros\n3-ambos')

if escolha == '1': 
    for i in range(numero):
        senha.append(choice(caracterLetra))

elif escolha == '2':
    for i in range(numero):
        senha.append(choice(caracter_Num))

elif escolha == '3':
    for i in range(numero):
        senha.append(choice(caracter_Num + caracterLetra))

else:
    print("escolha invalida")


for i in senha:
    print(i,end='')

