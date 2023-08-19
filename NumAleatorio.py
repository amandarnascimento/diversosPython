
#Crie um programa que escolha um numero aleatório entre 0 e 20 e peça ao usuário para tentar descobrir qual numero foi escolhido.
# solicitar ao usuario digitar um número ate ele acertar, ao acertar, o programa deve mostrar quantos palpites foram necessarios. 


from random import randint 

numero_aleatorio = randint(0, 20)
qnt_tentativas = 1
numero_usuario = -1


while numero_usuario != numero_aleatorio:
    numero_usuario = int(input('Digite um número ')) 

    if numero_aleatorio == numero_usuario:
        print('Você acertou!')
    else: 
        if numero_aleatorio < numero_usuario:
            print('Não acertou, o número é menor ')
        else:
            numero_aleatorio > numero_usuario
            print('Não acertou, o número é maior ')
        qnt_tentativas = qnt_tentativas + 1

print('Número de tentativas: ', qnt_tentativas)
