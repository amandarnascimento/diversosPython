#calculadora python

from funcoes import somar, subtrair

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))

while True:
    escolha = input('''
1 - somar
2 - subtrair 
3 - multiplicar
4 - dividir
5 - sair''')
    

    if escolha == '5':
        break
    if escolha == '1':
        print(somar(num1 = numero1, num2 = numero2))
        
    if escolha == '2':
        print(subtrair(numero1, numero2))
    if escolha == '3':
        print(multiplicar(numero1, numero2))
    if escolha =='4':
        print(dividir(numero1, numero2))
    





