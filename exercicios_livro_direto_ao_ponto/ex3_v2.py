def somar(num1, num2):
    soma = num1 + num2
    return print(f" A soma é {soma}")

def subtrair(num1, num2):
    subtracao = num1 - num2
    return print(f"A subtração é {subtracao}")

def multiplicar(num1, num2):
    multiplicacao = num1 * num2
    return print(f"A multiplicação é {multiplicacao}")

def divisao(num1, num2):
    if num2 != 0:
        dividir = num1 / num2
        return print(f"O resultado da divisão é {dividir}")
    else:
        print("Erro, divisão por zero")

def executar_acao(opcao, num1, num2):
    if opcao == 1:
        somar(num1, num2)
    elif opcao == 2:
        subtrair(num1, num2)
    elif opcao == 3:
        multiplicar(num1, num2)
    elif opcao == 4:
        divisao(num1, num2)
    else:
        print("Opção inválida")

print("\nEscolha a opção\n")
print("1 - Para somar")
print("2 - Para subtrair")
print("3 - Para multiplicar")
print("4 - Para dividir")
print("5 - Sair\n")

while True:

    try: 
        opcao = int(input("Digite a opção escolhida: "))
        
        if opcao == 5:
            print("Encerrando o programa")
            break

        if opcao not in [1, 2, 3, 4]:
            print("opção não existe, digite de novo: ")
            continue


        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        executar_acao(opcao, numero1, numero2)

        continuar = input("Deseja continuar? s para sim")
        if continuar == 's':
                continue
        else:
                break 

    except ValueError:
        print("Deu ruim...")

        

