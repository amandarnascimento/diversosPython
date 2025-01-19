def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Erro: divisão por zero!")
        return None

def executar_acao(opcao, num1, num2):
    if opcao == 1:
        resultado = somar(num1, num2)
        print(f"O resultado da soma é {resultado:.2f}")
    elif opcao == 2:
        resultado = subtrair(num1, num2)
        print(f"O resultado da subtração é {resultado:.2f}")
    elif opcao == 3:
        resultado = multiplicar(num1, num2)
        print(f"O resultado da multiplicação é {resultado:.2f}")
    elif opcao == 4:
        resultado = dividir(num1, num2)
        if resultado is not None:
            print(f"O resultado da divisão é {resultado:.2f}")
    else:
        print("Opção inválida")

print("\nEscolha a opção:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("5 - Sair")

while True:
    try:
        opcao_usuario = int(input("\nDigite a opção desejada: "))
        
        if opcao_usuario == 5:
            print("Encerrando o programa. Até mais!")
            break
        
        if opcao_usuario not in [1, 2, 3, 4]:
            print("Opção inválida! Tente novamente.")
            continue

        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        executar_acao(opcao_usuario, numero1, numero2)

        continuar = input("\nDeseja continuar? (s para sim): ").lower()
        if continuar != 's':
            print("Encerrando o programa. Obrigado!")
            break

    except ValueError:
        print("Erro: digite um número válido!")
