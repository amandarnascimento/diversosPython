#Criar um programa que leia 2 números e que o usuário possa escolher uma opção

opt = 0

while opt != 5:
    print('---------')
    print('[1] - Somar')
    print('[2] - Subtrair')
    print('[3] - Multiplicar')
    print('[4] - Dividir')
    print('[5] - Sair')
    print('---------')

    opt = int(input('>>>>>> Digite uma opção '))
    num1 = int(input('Digite um número '))
    num2 = int(input('Digite outro número '))

    if opt == 1:
        result = num1 + num2
        print('O resultado da soma é: ', result)  

    elif opt == 2:
        result = num1 - num2
        print('O resultado da subtração é: ', result)  

    elif opt == 3:
        result = num1 * num2
        print('O resultado da multiplicação é: ', result)    

    elif opt == 4:
        if num2 != 0:
            result = num1 / num2
            print('O resultado da divisão é: ', result)   
        else: print('Não existe divisão por zero ') 

    elif opt == 5:
        print('Fim do programa...')



print('Fim do programa')
