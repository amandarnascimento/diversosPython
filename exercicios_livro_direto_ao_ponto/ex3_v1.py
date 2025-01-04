def executar_acao(acao, num1, num2):
    if acao == 1:
        #chama a funcao somar
        somar(num1,num2)
    elif acao == 2:
        subtrair(num1, num2)
    elif acao == 3:
        multiplicar(num1,num2)  
    elif acao == 4:
        dividir(num1, num2) 
    else:
        print("Opção inválida!")


def somar(num1, num2):
    soma = num1 + num2
    return print(f"a soma é: {soma}")

def subtrair(num1, num2):
    subtracao = num1 - num2
    return print(f"a subtração é: {subtracao}")

def multiplicar(num1, num2):
    multiplicacao = num1 * num2
    return print(f"a multiplicação é: {multiplicacao}")

def dividir(num1, num2):
    if num2 != 0:
        divisao = num1 / num2
        print(f"a divisão é: {divisao}")
    else:
        print("Erro, divisão por zero")
    
while True:
    print("\nEscolha uma das opções abaixo:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair") 

    try:
        acao = int(input("Digite a opção desejada: "))
        if acao == 5:
            print("Encerrando o programa...")
            break

        
        if acao not in [1, 2, 3, 4]:
          print("Opção não existe! ")
          continue


        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))


        executar_acao(acao, numero1, numero2)

    except ValueError:
        print("Entrada inválida! Por favor, digite números válidos.")

#somar(numero1,numero2)
#subtrair(numero1, numero2)
#multiplicar(numero1,numero2)
#dividir(numero1, numero2)

